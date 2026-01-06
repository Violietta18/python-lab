def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(input_file_path, "r", encoding="utf-8", errors="ignore") as infile:
            for line in infile:
                parts = line.split()
                if parts:
                    ip = parts[0]
                    if ip in allowed_ips:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1

        with open(output_file_path, "w", encoding="utf-8") as outfile:
            for ip, count in ip_counts.items():
                outfile.write(f"{ip} - {count}\n")

    except FileNotFoundError:
        print(f"Файл не знайдено: {input_file_path}")
    except IOError:
        print("Помилка запису у файл")
