from epagneul.models.observables import Machine, User
from epagneul.models.relationships import SysmonLogonRelationship, RelationshipType


def parse_3(store, event):
    user = User()
    machine = Machine()

    initiated = None
    image = None
    protocol = None
    destination_port = None
    source_port = None

    # Iterate over key-value pairs in event.data
    for name, value in event.data.items():
        # skip empty or None values
        if not value:
            continue

        if name == "User":
            user.username = value
        elif name == "DestinationIp":
            machine.ip = value
        elif name == "DestinationHostname":
            machine.hostname = value
        elif name == "Image":
            image = value
        elif name == "Protocol":
            protocol = value
        elif name == "Initiated":
            initiated = value
        elif name == "SourcePort":
            source_port = value
        elif name == "DestinationPort":
            destination_port = value
        # Add other fields if needed

    user_id = store.add_user(user)
    machine_id = store.add_machine(machine)

    if user_id and machine_id:
        store.add_relationship(
            SysmonLogonRelationship(
                source=user_id,
                target=machine_id,
                event_type=RelationshipType.NETWORK_CONNECTION,
                timestamp=event.timestamp,
                initiated=initiated,
                image=image,
                procotol=protocol,  # or 'protocol' if you prefer consistent naming
                destination_port=destination_port,
                source_port=source_port,
            )
        )
