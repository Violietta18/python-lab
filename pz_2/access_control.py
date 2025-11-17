from user.administrator import Administrator
from user.regular_user import RegularUser
from user.guest_user import GuestUser
from user.user import User


class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)

        if user and user.verify_password(password) and user.is_active:
            if isinstance(user, RegularUser):
                user.update_login_time()
            return user

        return None
