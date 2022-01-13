from epagneul.models.relationships import NativeLogonRelationship, RelationshipType
from epagneul.models.observables import Machine, User


def parse_4648(store, event):
    user = User()
    machine = Machine()
    logon_type = 0
    status = ""
    for item in event.data:
        if not item.text:
            continue
        name = item.get("Name")
        if name == "SubjectUserSid":
            user.sid = item.text
        elif name == "SubjectUserName":
            user.username = item.text
        elif name == "SubjectDomainName":
            user.domain = item.text
        elif name == "TargetServerName":
            machine.hostname = item.text
        elif name == "TargetServerName":
            machine.hostname = item.text
        elif name == "TargetDomainName":
            machine.domain = item.text

    user_id = store.add_user(user)
    machine_id = store.add_machine(machine)

    if user_id and machine_id:
        store.add_relationship(
            NativeLogonRelationship(
                source=user_id,
                target=machine_id,
                event_type=RelationshipType.LOGON_EXPLICIT_CREDS,
                timestamp=event.timestamp,
                logon_type=logon_type,
                status=status,
            )
        )
