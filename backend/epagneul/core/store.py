from epagneul.models.relationships import BaseRelationship
from epagneul.models.observables import Machine, User, LocalAdminUser, DomainAdminUser, Group, ObservableType
import pandas as pd

from epagneul.core.algorithms import adetection

KNOWN_ADMIN_SIDS = {
    "S-1-5-18": "System (or LocalSystem)",
    "S-1-5-19": "NT Authority (LocalService)",
    "S-1-5-20": "Network Service",
    "S-1-5-32-544": "Administrator",
    "S-1-5-32-547": "Power User",
}

KNOWN_ADMIN_SIDS_ENDINGS = {
    "-500": "Domain local administrator",
    "-502": "krbtgt",
    "-512": "Domain Admin",
    "-517": "Cert Publisher",
    "-518": "Schema Admin",
    "-519": "Enterprise Admin",
    "-520": "Group Policy Creator Owner",
}


def is_local_admin(user):
    if not user.sid:
        return False, None

    for sid, role in KNOWN_ADMIN_SIDS.items():
        if sid == user.sid:
            return True, role
    return False, None

def is_domain_admin(user):
    if not user.sid:
        return False, None

    for sid, role in KNOWN_ADMIN_SIDS_ENDINGS.items():
        if user.sid.endswith(sid):
            return True, role
    return False, None


def merge_models(a, b):
    for b_field in b.__fields__:
        b_field_value = getattr(b, b_field)
        if not b_field_value:
            continue
        a_field_value = getattr(a, b_field)

        if a_field_value == b_field_value:
            continue
        try:
            if a_field_value in b_field_value:
                # a is a subset of b
                setattr(a, b_field, b_field_value)
            continue
        except TypeError:
            pass

        if not a_field_value:
            setattr(a, b_field, b_field_value)
    return a


class Datastore:
    def __init__(self):
        self._nodes = {
            ObservableType.USER: {},
            ObservableType.MACHINE: {},
            ObservableType.GROUP: {}
        }
        """
        self.machines = {}
        self.users = {}
        self.groups = {}
        """

        self.relationships = {}
        # self.ml_frame = pd.DataFrame(index=[], columns=["dates", "eventid", "username"])

        self.ml_list = []

        self.start_time = None
        self.end_time = None

    @property
    def groups(self):
        return self._nodes[ObservableType.GROUP]

    @property
    def users(self):
        return self._nodes[ObservableType.USER]

    @property
    def machines(self):
        return self._nodes[ObservableType.MACHINE]

    def finalize(self):
        # Remove duplicate machines
        known_machines = {}
        for k in list(self.machines.keys()):
            if self.machines[k].hostname:
                known_machines[k] = self.machines[k]
                del self._nodes[ObservableType.MACHINE][k]

        for machine in self.machines.values():
            if not machine.hostname and not any(
                machine.ip in km.ips for km in known_machines.values()
            ):
                known_machines[machine.id] = machine

        self._nodes[ObservableType.MACHINE] = known_machines


        # Remove duplicate users
        known_users = {}
        for k in list(self.users.keys()):
            if self.users[k].sid and self.users[k].username:
                known_users[k] = self.users[k]
                del  self._nodes[ObservableType.USER][k]

        for user in self.users.values():
            if user.username in known_users:
                known_users[user.username] = merge_models(
                    known_users[user.username], user
                )
            else:
                for k, v in known_users.items():
                    if user.username == v.username and (user.domain in v.domain or v.domain in user.domain):
                        known_users[k] = merge_models(known_users[k], user)
                        break
                else:
                    known_users[user.username] = user

        self._nodes[ObservableType.USER] = known_users

        users = self.users.values()
        machines = self.machines.values()
        groups = self.groups.values()

        users_keys = self.users.keys()
        machines_keys = self.machines.keys()
        groups_keys = self.groups.keys()

        def resolve_node(node, node_type):
            if node_type == ObservableType.USER and node not in users_keys:
                for u in users:
                    if node == u.sid or node == u.username:
                        return u.id
            elif node_type == ObservableType.MACHINE and node not in machines_keys:
                for m in machines:
                    if node== m.hostname or node in m.ips:
                        return m.id
            return node

        for event in self.relationships.values():

            event.source = resolve_node(event.source, event.source_type)
            event.target = resolve_node(event.target, event.target_type)

            for ts in event.timestamps:
                self.add_ml_frame([ts.strftime("%Y-%m-%d %H:%M:%S"), event.event_type, event.source])

            event.source = f"{event.source_type}-{event.source}"
            event.target = f"{event.target_type}-{event.target}"

        for user, rank in self.get_change_finder().items():
            if user in users_keys:
                self.users[user].rank = rank

    def add_timestamp(self, timestamp):
        if not self.start_time:
            self.start_time = timestamp
        elif self.start_time > timestamp:
            self.start_time = timestamp

        if not self.end_time:
            self.end_time = timestamp
        elif self.end_time < timestamp:
            self.end_time = timestamp

    """
    def get_timeline():
        count_set = pd.DataFrame(self.ml_list, columns=["dates", "eventid", "username"])
        count_set["count"] = count_set.groupby(["dates", "eventid", "username"])[
            "dates"
        ].transform("count")
        return count_set.drop_duplicates()
    """
    def get_change_finder(self):
        count_set = pd.DataFrame(self.ml_list, columns=["dates", "event", "username"])
        count_set["count"] = count_set.groupby(["dates", "event", "username"])["dates"].transform("count")
        count_set = count_set.drop_duplicates()
        tohours = int((self.end_time - self.start_time).total_seconds() / 3600)
        return adetection(count_set, list(self.users.keys()), self.start_time, tohours)

    def add_ml_frame(self, frame):
        self.ml_list.append(frame)
        # self.ml_frame = self.ml_frame.append(series, ignore_index=True)

    def add_relationship(self, event):
        identifier = f"{event.source}-{event.event_type}-{event.target}"
        if identifier in self.relationships:
            self.relationships[identifier].timestamps.add(event.timestamp)
            self.relationships[identifier].count = self.relationships[identifier].count + 1
        else:
            self.relationships[identifier] = BaseRelationship(
                **event.dict(exclude={"timestamp"}),
                timestamps={event.timestamp},
            )

    def add_machine(self, machine: Machine):
        if machine.hostname:
            machine.id = machine.hostname
        elif machine.ip:
            machine.id = machine.ip
        else:
            return None

        if machine.id in self.machines:
            self.machines[machine.id] = merge_models(self.machines[machine.id], machine)
        else:
            self.machines[machine.id] = machine
        self.machines[machine.id].add_ip(machine.ip)
        return machine.id

    def add_user(self, user: User):
        if not user.sid and not user.username:
            return None
        if user.sid and user.sid.count("-") != 3:
            user.id = user.sid
        else:
            user.id = user.username

        local_admin, role = is_local_admin(user)
        if not local_admin:
            domain_admin, role = is_domain_admin(user)

        if role:
            user.role = role
        
        if user.id in self.users:
            self.users[user.id] = merge_models(self.users[user.id], user)
        else:
            self.users[user.id] = user

        if local_admin:
            user_category = LocalAdminUser
        elif domain_admin or user.is_admin:
            user_category = DomainAdminUser
        else:
            user_category = User

        self.users[user.id] = user_category(**user.dict(exclude={"bg_opacity", "bg_color", "border_color", "shape", "tip", "width", "height", "border_width"}))
        return user.id

    def add_group(self, group: Group):
        if not group.name and not group.sid:
            return None

        if group.sid and group.sid.count("-") != 3:
            group.id = group.sid
        else:
            group.id = group.username

        if group.id in self.groups:
            self.groups[group.id] = merge_models(self.groups[group.id], group)
        else:
            self.groups[group.id] = group

        return group.id