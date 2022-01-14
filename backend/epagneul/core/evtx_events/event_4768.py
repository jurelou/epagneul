import ipaddress

from epagneul.models.relationships import NativeLogonRelationship, RelationshipType
from epagneul.models.observables import Machine, User


def parse_4768(store, event):
    user = User()
    machine = Machine()

    service_name = None
    relationship_type = None
    ticket_options = None
    pre_auth_type = None
    cert_issuer_name = None
    cert_serial_number = None

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
        elif name == "ServiceName":
            service_name = item.text
        elif name == "TicketOptions":
            ticket_options = item.text
        elif name == "TicketEncryptionType":
            if item.text == "0x1":
                relationship_type = RelationshipType.TGT_DES_REQUEST
            elif item.text == "0x3":
                relationship_type = RelationshipType.TGT_DES_REQUEST
            elif item.text == "0x11":
                relationship_type = RelationshipType.TGT_AES_REQUEST
            elif item.text == "0x12":
                relationship_type = RelationshipType.TGT_AES_REQUEST
            elif item.text == "0x17":
                relationship_type = RelationshipType.TGT_RC4_REQUEST
            elif item.text == "0x18":
                relationship_type = RelationshipType.TGT_RC4_REQUEST
        elif name == "PreAuthType":
            if item.text == "2":
                pre_auth_type = "password authentication"
            elif item.text =="11":
                pre_auth_type = "PA-ETYPE-INFO"            
            elif item.text =="15":
                pre_auth_type = "Smart Card logon"
            else:
                pre_auth_type = item.text
        elif name == "CertIssuerName":
            cert_issuer_name = item.text
        elif name == "CertSerialNumber":
            cert_serial_number = item.text

    user_id = store.add_user(user)
    machine_id = store.add_machine(machine)

    if user_id and machine_id and relationship_type:
        store.add_relationship(
            NativeLogonRelationship(
                source=user_id,
                target=machine_id,
                event_type=relationship_type,
                timestamp=event.timestamp,
                service_name = service_name,
                ticket_options = ticket_options,
                pre_auth_type = pre_auth_type,
                cert_issuer_name = cert_issuer_name,
                cert_serial_number = cert_serial_number
            )
        )
