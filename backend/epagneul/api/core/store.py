from epagneul.models.events import BaseEvent
from epagneul.models.observables import Machine, User

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


def get_role_from_sid(user):
    if not user.sid:
        return False, None

    for sid, role in KNOWN_ADMIN_SIDS.items():
        if sid == user.sid:
            return True, role

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

        if a_field_value:
            print(f"DOUBLE VALUE ({b_field}) {a_field_value} -- {b_field_value}")
        else:
            setattr(a, b_field, b_field_value)
    return a


class Datastore:
    def __init__(self):
        self.machines = {}
        self.users = {}
        self.logon_events = {}
        # self.ml_frame = pd.DataFrame(index=[], columns=["dates", "eventid", "username"])

        self.ml_list = []

        self.start_time = None
        self.end_time = None

    def finalize(self):
        # Remove duplicate machines
        known_machines = {}
        for k in list(self.machines.keys()):
            if self.machines[k].hostname:
                known_machines[k] = self.machines[k]
                del self.machines[k]

        for machine in self.machines.values():
            if not machine.hostname and not any(
                machine.ip in km.ips for km in known_machines.values()
            ):
                known_machines[machine.id] = machine

        self.machines = known_machines

        # Remove duplicate users
        known_users = {}
        for k in list(self.users.keys()):
            if self.users[k].sid and self.users[k].username:
                known_users[k] = self.users[k]
                del self.users[k]

        for user in self.users.values():
            if user.username in known_users:
                known_users[user.username] = merge_models(
                    known_users[user.username], user
                )
            else:
                for k, v in known_users.items():
                    if user.username == v.username and user.domain == v.domain:
                        known_users[k] = merge_models(known_users[k], user)
                        break
                else:
                    known_users[user.username] = user
        self.users = known_users

        for event in self.logon_events.values():
            if event.target not in self.machines:
                for m in self.machines.values():
                    if event.target == m.hostname or event.target in m.ips:
                        event.target = m.id
                        break
            if event.source not in self.users:
                for u in self.users.values():
                    if event.source == u.sid or event.source == u.username:
                        event.source = u.id
                        break
            event.source = f"user-{event.source}"
            event.target = f"machine-{event.target}"
            for ts in event.timestamps:
                self.add_ml_frame(
                    [ts.strftime("%Y-%m-%d %H:%M:%S"), event.event_type, event.source]
                )

    def add_timestamp(self, timestamp):
        if not self.start_time:
            self.start_time = timestamp
        elif self.start_time > timestamp:
            self.start_time = timestamp

        if not self.end_time:
            self.end_time = timestamp
        elif self.end_time < timestamp:
            self.end_time = timestamp

    def get_timeline():
        count_set = pd.DataFrame(self.ml_list, columns=["dates", "eventid", "username"])
        count_set["count"] = count_set.groupby(["dates", "eventid", "username"])[
            "dates"
        ].transform("count")
        return count_set.drop_duplicates()

    def get_change_finder(self):
        count_set = pd.DataFrame(self.ml_list, columns=["dates", "eventid", "username"])
        count_set["count"] = count_set.groupby(["dates", "eventid", "username"])[
            "dates"
        ].transform("count")
        count_set = count_set.drop_duplicates()
        tohours = int((self.end_time - self.start_time).total_seconds() / 3600)
        return adetection(count_set, list(self.users.keys()), self.start_time, tohours)

    def add_ml_frame(self, frame):
        self.ml_list.append(frame)
        # self.ml_frame = self.ml_frame.append(series, ignore_index=True)

    def add_logon_event(self, event):
        identifier = f"{event.source}-{event.event_type}-{event.target}"
        if identifier in self.logon_events:
            self.logon_events[identifier].timestamps.add(event.timestamp)
        else:
            self.logon_events[identifier] = BaseEvent(
                **event.dict(exclude={"timestamp", "timestamps"}),
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
        if user.sid:
            # SID
            if user.sid.count("-") != 3:
                user.id = user.sid
            else:
                user.id = user.username
        elif user.username:
            user.id = user.username
        else:
            return None

        user.is_admin, user.role = get_role_from_sid(user)

        if user.id in self.users:
            self.users[user.id] = merge_models(self.users[user.id], user)
        else:
            self.users[user.id] = user

        return user.id
