from epagneul.models.observables import User, Machine
from epagneul.models.events import NativeLogonEvent
import ipaddress

def parse_basic_logons(store, event):
    user = User()
    machine = Machine()
    logon_type = 0
    status = ""

    for item in event.data:
        if not item.text:
            continue
        name = item.get("Name")
        if name in ("WorkstationName", "Workstation"):
            machine.hostname = item.text
        elif name == "IpAddress":
            value = item.text.replace("::ffff:", "")
            try:
                ipaddress.ip_address(value)
                machine.ip = value
            except:
                machine.hostname = value
        elif name == "TargetUserName":
            user.username = item.text
        elif name == "TargetDomainName":
            user.domain = item.text
        elif name in ("TargetUserSid", "TargetSid"):
            user.sid = item.text
        #elif name == "SubjectDomainName" :
        #    store.add_domain(Domain(name=item.text))
        elif name == "LogonType":
            logon_type = item.text
        elif name == "Status":
            status = item.text
        #elif name == "AuthenticationPackageName":
        #    relationship_data["AuthenticationPackageName"] = item.text

    user_id = store.add_user(user)
    machine_id = store.add_machine(machine)

    if user_id and machine_id:
        store.add_logon_event(NativeLogonEvent(
            source=user_id,
            target=machine_id,
            event_type=event.event_id,
            timestamp=event.timestamp,
            logon_type=logon_type,
            status=status
        ))