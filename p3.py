#Accept a number as input, say X and define a logic to get the output say Y. The Input can be only 0 or 1 and the output must be 1 if input is 0 and vicevesa. Do not use Boolean Alzeb

X = int(input('Enter the input number(0 or 1 only:)'))

if X ==0 or X ==1:
    Y = 1 - X
    print(f'Input number = {X}, Output number ={Y}')
else:
    print('invalid input')