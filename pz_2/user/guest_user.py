from .user import User

class GuestUser(User):
    def __init__(self, username="guest", password="guest", is_active=True):
        super().__init__(username, password, is_active)
        self.read_only = True
