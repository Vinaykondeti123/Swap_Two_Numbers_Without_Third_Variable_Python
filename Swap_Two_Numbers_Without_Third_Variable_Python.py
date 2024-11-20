# swapping of two numbers without third varaible
a=float(input('Enter first Number: '))
b=float(input('Enter second Number: '))
a=a+b          #b=b+a
b=a-b          #a=b-a
a=a-b          #b=b-a
print(f'Value of First Number: {a}')
print(f'Value of Second Number: {b}')