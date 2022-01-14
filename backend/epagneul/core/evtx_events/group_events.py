import ipaddress

from epagneul.models.relationships import GroupRelationship, RelationshipType
from epagneul.models.observables import Group, User


def parse_add_group(store, event):
    user = User()
    subject = User()
    group = Group()

    privs = None

    for item in event.data:
        if not item.text:
            continue
        name = item.get("Name")
        if name == "TargetUserName":
            group.name = item.text
        elif name == "TargetDomainName":
            group.domain = item.text
        elif name == "TargetSid":
            group.sid = item.text
        elif name == "MemberSid":
            user.sid = item.text
        elif name == "SubjectUserSid":
            subject.sid = item.text
        elif name == "SubjectUserName":
            subject.username = item.text
        elif name == "SubjectDomainName":
            subject.domain = item.text
        elif name == "PrivilegeList":
            privs = item.text

    store.add_user(subject)

    user_id = store.add_user(user)
    group_id = store.add_group(group)

    if user_id and group_id:
        store.add_relationship(
            GroupRelationship(
                source=user_id,
                target=group_id,
                event_type=RelationshipType.GROUP_ADDED,
                timestamp=event.timestamp,
                privileges=privs
            )
        )

