import sqlite3
import hashlib

def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(login, password, full_name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute("""
            INSERT INTO users (login, password, full_name)
            VALUES (?, ?, ?)
        """, (login, hashed_password, full_name))

        conn.commit()
        print(" Користувача успішно додано")
    except sqlite3.IntegrityError:
        print(" Користувач з таким логіном вже існує")
    finally:
        conn.close()

def update_password(login, new_password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed_password = hash_password(new_password)

    cursor.execute("""
        UPDATE users
        SET password = ?
        WHERE login = ?
    """, (hashed_password, login))

    if cursor.rowcount == 0:
        print(" Користувача не знайдено")
    else:
        print(" Пароль успішно оновлено")

    conn.commit()
    conn.close()

def authenticate_user(login):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT password FROM users WHERE login = ?
    """, (login,))

    result = cursor.fetchone()
    conn.close()

    if not result:
        print(" Користувача не знайдено")
        return

    stored_hash = result[0]
    entered_password = input("Введіть пароль: ")
    entered_hash = hash_password(entered_password)

    if entered_hash == stored_hash:
        print(" Автентифікація успішна")
    else:
        print(" Невірний пароль")


if __name__ == "__main__":
    create_db()

    while True:
        print("\n1 - Додати користувача")
        print("2 - Оновити пароль")
        print("3 - Автентифікація")
        print("0 - Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            login = input("Логін: ")
            password = input("Пароль: ")
            full_name = input("ПІБ: ")
            add_user(login, password, full_name)

        elif choice == "2":
            login = input("Логін: ")
            new_password = input("Новий пароль: ")
            update_password(login, new_password)

        elif choice == "3":
            login = input("Логін: ")
            authenticate_user(login)

        elif choice == "0":
            break

        else:
            print(" Невірний вибір")
