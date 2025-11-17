from user.administrator import Administrator
from user.regular_user import RegularUser
from user.guest_user import GuestUser
from access_control import AccessControl


def main():
    system = AccessControl()

    admin = Administrator("admin", "admin123", permissions=["manage_users"])
    user = RegularUser("ivan", "qwerty")
    guest = GuestUser("guest")

    system.add_user(admin)
    system.add_user(user)
    system.add_user(guest)

    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    logged_user = system.authenticate_user(username, password)

    if logged_user:
        print(f"Вхід успішний! Вітаємо, {logged_user.username}")
    else:
        print("Невірний логін або пароль")


if __name__ == "__main__":
    main()
