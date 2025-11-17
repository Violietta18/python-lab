from .user import User


class Administrator(User):
    def __init__(self, username, password, permissions=None, is_active=True):
        super().__init__(username, password, is_active)
        self.permissions = permissions if permissions is not None else []

    def add_permission(self, permission):
        self.permissions.append(permission)