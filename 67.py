def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_number(int(input("Enter any number : "))))
