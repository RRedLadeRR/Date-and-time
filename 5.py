#Timofey

def calculate_happiness(number):
    while len(str(number)) > 1:
        number = sum(int(digit) for digit in str(number))
    return number

with open('6_yyyymmdd.txt', 'r') as input_file:
    date_str = input_file.read().strip()

date_number = int(date_str)

happiness_number = calculate_happiness(date_number)

with open('6_happydate.txt', 'w') as output_file:
    output_file.write(str(happiness_number))

print(f"Щасливість дати: {happiness_number}")