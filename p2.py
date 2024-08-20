##Read a number from the user and check if it is an Even number or not.


my_number = int(input('Enter a number to check if it is Even or not:'))



if my_number % 2 == 0:
    print(my_number, 'is a Even number')
else:
    print(f'{my_number} is not an even number')