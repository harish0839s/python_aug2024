#Program to Find Odd placed Even digits in a number
number = int(input("ENTER A NUMBER TO REVERSE A NUMBER:"))
number_str = str(number)
odd_position_even_digits = []
for index, digit in enumerate(number_str):
    position = index + 1
    if position % 2 != 0 and int(digit) % 2 == 0:
        odd_position_even_digits.append(digit)
print("Even digits in odd positions:", ''.join(odd_position_even_digits)) 
