# Program to Find Sum of digits of a number

number = input("Enter the number you want to find the sum of digits: ")
sum = 0
for i in number:
    x=int(i)
    sum = sum + x
print(sum)