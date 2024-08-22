
number = 123456  
number_str = str(number)
position_type = 'odd'  
odd_position_digits = []
even_position_digits = []
for index, digit in enumerate(number_str):
    position = index + 1
    if position % 2 != 0:
        if position_type == 'odd':
            odd_position_digits.append(digit)
    else:
        if position_type == 'even':
            even_position_digits.append(digit)
if position_type == 'odd':
    print("Digits in odd positions:", ''.join(odd_position_digits))
else:
    print("Digits in even positions:", ''.join(even_position_digits))