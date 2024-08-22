number = int(input("ENTER A NUMBER TO PRINT SUM OF EVEN NUMBERS:"))
digit_type = 'even' 
number = abs(number)
total_sum = 0
for digit in str(number):
    digit = int(digit)
    if digit_type == 'even' and digit % 2 == 0:
        total_sum += digit
    elif digit_type == 'odd' and digit % 2 != 0:
        total_sum += digit
print("Sum of", digit_type, "digits:", total_sum)