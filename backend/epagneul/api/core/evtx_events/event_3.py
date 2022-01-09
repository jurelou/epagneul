from epagneul.models.events import SysmonLogonEvent
from epagneul.models.observables import Machine, User


def parse_3(store, event):

    user = User()
    machine = Machine()

    initiated = None
    image = None
    procotol = None
    destination_port = None
    source_port = None

    for item in event.data:
        if not item.text:
            continue

        name = item.get("Name")
        if name == "User":
            user.username = item.text
        elif name == "DestinationIp":
            machine.ip = item.text
        elif name == "DestinationHostname":
            machine.hostname = item.text
        elif name == "Image":
            image = item.text
        elif name == "Protocol":
            procotol = item.text
        elif name == "Initiated":
            initiated = item.text
        elif name == "SourcePort":
            source_port = item.text
        elif name == "DestinationPort":
            destination_port = item.text

    user_id = store.add_user(user)
    machine_id = store.add_machine(machine)

    if user_id and machine_id:
        store.add_logon_event(
            SysmonLogonEvent(
                source=user_id,
                target=machine_id,
                event_type=event.event_id,
                timestamp=event.timestamp,
                initiated=initiated,
                image=image,
                procotol=procotol,
                destination_port=destination_port,
                source_port=source_port,
            )
        )
