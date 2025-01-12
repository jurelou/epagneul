import ipaddress

from epagneul.models.relationships import NativeLogonRelationship, RelationshipType
from epagneul.models.observables import Machine, User


def parse_4768(store, event):
    """EventID 4768: A Kerberos authentication ticket (TGT) was requested (JSON version)."""
    user = User()
    machine = Machine()

    service_name = None
    relationship_type = None
    ticket_options = None
    pre_auth_type = None
    cert_issuer_name = None
    cert_serial_number = None

    # Iterate over key-value pairs in event.data
    for name, value in event.data.items():
        if not value:  # skip empty or None values
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
                machine.hostname = ipaddr
        elif name == "TargetUserName":
            user.username = value
        elif name == "TargetDomainName":
            user.domain = value
        elif name in ("TargetUserSid", "TargetSid"):
            user.sid = value
        elif name == "ServiceName":
            service_name = value
        elif name == "TicketOptions":
            ticket_options = value
        elif name == "TicketEncryptionType":
            if value == "0x1":
                relationship_type = RelationshipType.TGT_DES_REQUEST
            elif value == "0x3":
                relationship_type = RelationshipType.TGT_DES_REQUEST
            elif value == "0x11":
                relationship_type = RelationshipType.TGT_AES_REQUEST
            elif value == "0x12":
                relationship_type = RelationshipType.TGT_AES_REQUEST
            elif value == "0x17":
                relationship_type = RelationshipType.TGT_RC4_REQUEST
            elif value == "0x18":
                relationship_type = RelationshipType.TGT_RC4_REQUEST
        elif name == "PreAuthType":
            if value == "2":
                pre_auth_type = "password authentication"
            elif value == "11":
                pre_auth_type = "PA-ETYPE-INFO"
            elif value == "15":
                pre_auth_type = "Smart Card logon"
            else:
                pre_auth_type = value
        elif name == "CertIssuerName":
            cert_issuer_name = value
        elif name == "CertSerialNumber":
            cert_serial_number = value

    # Add the user and machine to the store
    user_id = store.add_user(user)
    machine_id = store.add_machine(machine)

    # Add relationship if relevant
    if user_id and machine_id and relationship_type:
        store.add_relationship(
            NativeLogonRelationship(
                source=user_id,
                target=machine_id,
                event_type=relationship_type,
                timestamp=event.timestamp,
                service_name=service_name,
                ticket_options=ticket_options,
                pre_auth_type=pre_auth_type,
                cert_issuer_name=cert_issuer_name,
                cert_serial_number=cert_serial_number
            )
        )
