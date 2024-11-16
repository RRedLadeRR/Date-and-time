#Timofey

try:
    with open('7_input.txt', 'r') as file:
        n = int(file.readline().strip())
        days = list(map(int, file.readline().strip().split()))

    weeks = []
    current_week_days = 0

    for day in days:
        if day == 1:
            current_week_days += 1
        elif day == 0 and current_week_days > 0:
            weeks.append(current_week_days)
            current_week_days = 0

    if current_week_days > 0:
        weeks.append(current_week_days)

    k = len(weeks)

    with open('7_output.txt', 'w') as file:
        file.write(f"{k}\n")
        file.write(" ".join(map(str, weeks)))
    print("Відповідь записано у файл 7_output.txt.")

except FileNotFoundError:
    print("Файл 7_input.txt не знайдено.")
except Exception as e:
    print(f"Сталася помилка: {e}")