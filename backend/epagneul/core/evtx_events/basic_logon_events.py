import ipaddress

from epagneul.models.relationships import NativeLogonRelationship, RelationshipType
from epagneul.models.observables import Machine, User


def _parse_basic_logons(store, event, relationship_type):
    user = User()
    machine = Machine()
    logon_type = 0
    status = ""

    # iterate over key-value pairs:
    for name, value in event.data.items():
        if not value:  # skip empty values
            continue

        if name in ("WorkstationName", "Workstation"):
            machine.hostname = value
        elif name == "IpAddress":
            # remove "::ffff:" if present
            ipaddr = value.replace("::ffff:", "")
            try:
                ipaddress.ip_address(ipaddr)
                machine.ip = ipaddr
            except ValueError:
                # Not a valid IP, treat as hostname
                machine.hostname = value
        elif name == "TargetUserName":
            user.username = value
        elif name == "TargetDomainName":
            user.domain = value
        elif name in ("TargetUserSid", "TargetSid"):
            user.sid = value
        elif name == "LogonType":
            logon_type = value
        elif name == "Status":
            status = value
        # Add other fields if needed

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


def parse_tgt_failed(store, event):
    _parse_basic_logons(store, event, RelationshipType.TGT_FAILED)

def parse_tgs(store, event):
    _parse_basic_logons(store, event, RelationshipType.TGS_REQUEST)

def parse_ntlm_request(store, event):
    _parse_basic_logons(store, event, RelationshipType.NTLM_REQUEST)

