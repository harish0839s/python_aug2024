
number = int(input("ENTER A NUMBER TO REVERSE A NUMBER:"))
original_number = number
number = abs(number)
reversed_number = 0
while number > 0:
    last_digit = number % 10
    reversed_number = (reversed_number * 10) + last_digit
    number = number // 10
if original_number < 0:
    reversed_number = -reversed_number
print("Reversed number:", reversed_number)