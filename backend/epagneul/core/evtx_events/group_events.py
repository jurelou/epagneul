import ipaddress

from epagneul.models.relationships import GroupRelationship, RelationshipType
from epagneul.models.observables import Group, User


def parse_add_group(store, event):
    """Adaptation for adding users to groups via JSON data."""
    user = User()
    subject = User()
    group = Group()

    privs = None

    # Iterate over key-value pairs in event.data
    for name, value in event.data.items():
        if not value:  # skip empty or None values
            continue

        if name == "TargetUserName":
            group.name = value
        elif name == "TargetDomainName":
            group.domain = value
        elif name == "TargetSid":
            group.sid = value
        elif name == "MemberSid":
            user.sid = value
        elif name == "SubjectUserSid":
            subject.sid = value
        elif name == "SubjectUserName":
            subject.username = value
        elif name == "SubjectDomainName":
            subject.domain = value
        elif name == "PrivilegeList":
            privs = value

    # Add the subject (the one performing the action)
    store.add_user(subject)

    # Add the user being added to the group
    user_id = store.add_user(user)

    # Add the group
    group_id = store.add_group(group)

    # Create a relationship if both user and group are valid
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
