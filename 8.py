#Timofey

from datetime import date

birth_year = int(input("Введіть рік народження: "))
birth_month = int(input("Введіть місяць народження (1-12): "))
birth_day = int(input("Введіть день народження (1-31): "))

birth_date = date(birth_year, birth_month, birth_day)

current_date = date.today()

years = current_date.year - birth_date.year

if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    years -= 1

months = current_date.month - birth_date.month
if months < 0:
    months += 12

if current_date.day < birth_date.day:
    prev_month = current_date.replace(month=current_date.month - 1) if current_date.month > 1 else current_date.replace(month=12, year=current_date.year - 1)
    prev_month_days = (current_date.replace(year=prev_month.year, month=prev_month.month, day=1) - prev_month.replace(year=prev_month.year, month=prev_month.month, day=1)).days
    days = prev_month_days - (birth_date.day - current_date.day)
else:
    days = current_date.day - birth_date.day

print(f"Ваш вік: {years} років, {months} місяців, {days} днів.")