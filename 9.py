#Timofey

from datetime import datetime

date_input = input("Введіть дату через пробіл (рік місяць день): ")
time_input = input("Введіть час через пробіл (години хвилини секунди): ")

year, month, day = map(int, date_input.split())
hour, minute, second = map(int, time_input.split())

specified_datetime = datetime(year, month, day, hour, minute, second)

current_datetime = datetime.now()

time_difference = current_datetime - specified_datetime

days = time_difference.days
seconds = time_difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"{days} днів, {hours} години, {minutes} хвилин, {seconds} секунд")