#Timofey

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
print("Відповідь записано у файл 7_output.txt. Зверніть увагу що у вас повинен бути створений файл 7_input.txt з вхідними данними")