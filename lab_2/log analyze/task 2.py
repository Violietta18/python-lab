import hashlib

def generate_file_hashes(*file_paths):
    hashes = {}

    for path in file_paths:
        try:
            sha256 = hashlib.sha256()
            with open(path, "rb") as file:
                for chunk in iter(lambda: file.read(4096), b""):
                    sha256.update(chunk)

            hashes[path] = sha256.hexdigest()

        except FileNotFoundError:
            print(f"Файл не знайдено: {path}")
        except IOError:
            print(f"Помилка читання файлу: {path}")

    return hashes
