from epagneul.models.relationships import NativeLogonRelationship, RelationshipType

from epagneul.models.observables import Machine, User


def parse_4648(store, event):
    user = User()
    machine = Machine()
    logon_type = 0
    status = ""

    # Iterate over key-value pairs in event.data
    for name, value in event.data.items():
        # skip empty or None values
        if not value:
            continue

        if name == "SubjectUserSid":
            user.sid = value
        elif name == "SubjectUserName":
            user.username = value
        elif name == "SubjectDomainName":
            user.domain = value
        elif name == "TargetServerName":
            machine.hostname = value
        elif name == "TargetDomainName":
            machine.domain = value
        # add other fields if needed

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
