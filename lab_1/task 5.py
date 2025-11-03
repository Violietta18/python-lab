# Аутентифікація користувачів
# Ключ — логін, значення — словник з паролем та ПІБ

import hashlib

users = {
    "violietta18": {
        "password": hashlib.md5("qwerty".encode()).hexdigest(),
        "full_name": "Нечитайло Віолєтта Миколаївна"
    },
    "nastya23": {
        "password": hashlib.md5("12345".encode()).hexdigest(),
        "full_name": "Анастасія"
    },
    "alex2": {
        "password": hashlib.md5("00000".encode()).hexdigest(),
        "full_name": "Олександр"
    }
}

def check_password():
    """
    Перевіряє логін і пароль користувача.
    """
    login = input("Введіть логін: ")

    if login not in users:
        print("Користувача з таким логіном не існує.")
        return False

    entered_password = input("Введіть пароль: ")
    hashed_password = hashlib.md5(entered_password.encode()).hexdigest()

    if hashed_password == users[login]["password"]:
        print(f"Вітаємо, {users[login]['full_name']}! Доступ дозволено.")
        return True
    else:
        print("Невірний пароль. Доступ заборонено.")
        return False

check_password()
# Паролі для логінів:
# violietta18  — qwerty
# nastya23  — 12345
# alex2  — 00000