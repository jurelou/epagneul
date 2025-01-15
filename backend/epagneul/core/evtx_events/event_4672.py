from epagneul.models.observables import DomainAdminUser


def parse_4672(store, event):
    """EventID 4672: Special privileges assigned to new logon (JSON version)."""
    user = DomainAdminUser()
    
    # Iterate over key-value pairs in event.data
    for name, value in event.data.items():
        if not value:  # skip empty or None values
            continue
        
        if name == "SubjectUserName":
            user.username = value
        elif name == "SubjectUserSid":
            user.sid = value
        elif name == "SubjectDomainName":
            user.domain = value

    # Add the user to the store
    store.add_user(user)
