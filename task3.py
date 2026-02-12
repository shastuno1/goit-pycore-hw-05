import sys
def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return {}

    date = parts[0]
    time = parts[1]
    level = parts[2]
    message = parts[3]

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print("Файл не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return list(filter(lambda log: log.get("level") == level, logs))


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python task3.py <шлях_до_файлу> [рівень]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


