def analyze_log_file(log_file_path):
    response_codes = {}

    try:
        with open(log_file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                parts = line.split()
                for part in parts:
                    if part.isdigit() and len(part) == 3:
                        response_codes[part] = response_codes.get(part, 0) + 1
                        break

    except FileNotFoundError:
        print(f"Файл не знайдено: {log_file_path}")
    except IOError:
        print(f"Помилка читання файлу: {log_file_path}")

    return response_codes
