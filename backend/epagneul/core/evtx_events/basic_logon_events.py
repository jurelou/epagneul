import ipaddress

from epagneul.models.relationships import NativeLogonRelationship, RelationshipType
from epagneul.models.observables import Machine, User


def _parse_basic_logons(store, event, relationship_type):
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
        # elif name == "SubjectDomainName" :
        #    store.add_domain(Domain(name=item.text))
        elif name == "LogonType":
            logon_type = item.text
        elif name == "Status":
            status = item.text
        # elif name == "AuthenticationPackageName":
        #    relationship_data["AuthenticationPackageName"] = item.text

    user_id = store.add_user(user)
    machine_id = store.add_machine(machine)

    if user_id and machine_id:
        store.add_relationship(
            NativeLogonRelationship(
                source=user_id,
                target=machine_id,
                event_type=relationship_type,
                timestamp=event.timestamp,
                logon_type=logon_type,
                status=status,
            )
        )

def parse_logon_successfull(store, event):
    _parse_basic_logons(store, event, RelationshipType.SUCCESSFULL_LOGON)

def parse_logon_failed(store, event):
    _parse_basic_logons(store, event, RelationshipType.FAILED_LOGON)

def parse_tgt(store, event):
    _parse_basic_logons(store, event, RelationshipType.TGT_REQUEST)

def parse_tgt_failed(store, event):
    _parse_basic_logons(store, event, RelationshipType.TGT_FAILED)

def parse_tgs(store, event):
    _parse_basic_logons(store, event, RelationshipType.TGS_REQUEST)

def parse_ntlm_request(store, event):
    _parse_basic_logons(store, event, RelationshipType.NTLM_REQUEST)