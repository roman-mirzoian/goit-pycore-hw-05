import sys
from collections import Counter

log_levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']

def parse_log_line(line: str) -> dict:
    splitter_log = line.split(" ")
    return {
        "date": splitter_log[0],
        "time": splitter_log[1],
        "level": splitter_log[2],
        "message": " ".join(splitter_log[3:]).strip(),
    }

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"].upper() == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    return (Counter(log["level"] for log in logs))

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<20} | {'Кількість':<8}")
    print("-" * 21 + "|" + "-" * 10)
    
    for level in log_levels:
        count = counts.get(level, 0)
        print(f"{level:<20} | {count:<8}")
    return counts

def load_logs(file_path: str) -> list:
    parsed_logs = []
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            parsed_logs.append(parse_log_line(line))
    return parsed_logs

def main():
    file_path = None
    log_level = None

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Треба вказати шлях до файлу з логами.")
        sys.exit(1)

    if len(sys.argv) > 2:
        log_level = sys.argv[2]

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return
    
    display_log_counts(count_logs_by_level(logs))

    if log_level != None:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if len(filtered_logs) > 0:
            print(f"\nДеталі логів для рівня '{log_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else: 
            print(f"Логи для рівня '{log_level}' не знайдені")

if __name__ == "__main__":
    main()
