from epagneul.models.observables import DomainAdminUser


def parse_4672(store, event):
    """EventID 4672: Special privileges assigned to new logon."""
    user = DomainAdminUser()
    for item in event.data:
        if not item.text:
            continue
        name = item.get("Name")
        if name == "SubjectUserName":
            user.username = item.text
        elif name == "SubjectUserSid":
            user.sid = item.text
        elif name == "SubjectDomainName":
            user.domain = item.text
    store.add_user(user)
