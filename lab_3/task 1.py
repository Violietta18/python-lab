import sqlite3
import hashlib


# Функція для підключення до БД та створення таблиці
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn


# Функція для хешування пароля (щоб не зберігати його у відкритому вигляді)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# а) Додавання нового користувача
def add_user(login, password, full_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_pw = hash_password(password)
    try:
        cursor.execute('INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)',
                       (login, hashed_pw, full_name))
        conn.commit()
        print(f"Користувач {login} успішно доданий!")
    except sqlite3.IntegrityError:
        print("Помилка: Користувач з таким логіном вже існує.")
    finally:
        conn.close()


# б) Оновлення паролю
def update_password(login, new_password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_pw = hash_password(new_password)
    cursor.execute('UPDATE users SET password = ? WHERE login = ?', (hashed_pw, login))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Пароль для {login} оновлено.")
    else:
        print("Користувача не знайдено.")
    conn.close()


# в) Перевірка автентифікації
def authenticate():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE login = ?', (login,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == hash_password(password):
        print("Вхід успішний! Вітаємо.")
        return True
    else:
        print("Невірний логін або пароль.")
        return False


# Демонстрація роботи (можна видалити або змінити)
if __name__ == "__main__":
    init_db()  # Створюємо базу при першому запуску

    print("--- Реєстрація ---")
    u_login = input("Новий логін: ")
    u_pass = input("Новий пароль: ")
    u_name = input("Повне ім'я: ")
    add_user(u_login, u_pass, u_name)

    print("\n--- Перевірка входу ---")
    authenticate()
