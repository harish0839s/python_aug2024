##Program to Print X shape inside Hollow Square
def print_x_in_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end='')
            elif j == i or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
n = int(input("Enter the number of lines (odd number): "))
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    print_x_in_hollow_square(n)
