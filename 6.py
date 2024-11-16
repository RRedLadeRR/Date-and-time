#Timofey

from datetime import date

year1 = int(input("Введіть рік першої дати: "))
month1 = int(input("Введіть місяць першої дати (1-12): "))
day1 = int(input("Введіть день першої дати (1-31): "))

year2 = int(input("Введіть рік другої дати: "))
month2 = int(input("Введіть місяць другої дати (1-12): "))
day2 = int(input("Введіть день другої дати (1-31): "))

date1 = date(year1, month1, day1)
date2 = date(year2, month2, day2)

delta = date2 - date1

print(f"Кількість днів між датами: {delta.days}")