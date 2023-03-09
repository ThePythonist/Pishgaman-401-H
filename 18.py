number = int(input("Enter any number : "))
status = None

if number % 2 != 0:
    status = 'Odd'
else:
    status = 'Even'

print('The number is', status)
