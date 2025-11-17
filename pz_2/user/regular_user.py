from .user import User

class RegularUser(User):
    def __init__(self, username, password, last_login=None, is_active=True):
        super().__init__(username, password, is_active)
        self.last_login = last_login