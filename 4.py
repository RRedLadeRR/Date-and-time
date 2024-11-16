#Timofey

from datetime import datetime

now = datetime.now()

print("Current date and time:", now)
print("Current year:", now.year)
print("Month of year:", now.strftime("%B"))
print("Week number of the year:", now.strftime("%U"))
print("Day of year:", now.timetuple().tm_yday)
print("Day of the month:", now.day)
print("Day of week:", now.strftime("%A"))