def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


def main():
    entry = input("Enter any number to see the factorial : ")

    try:
        entry = int(entry)
        try:
            print(factorial(entry))
        except RecursionError:
            if entry == 0:
                print("Factorial of zero is 1")
            else:
                print("Number must be greater than zero! Try again")
                main()
    except ValueError:
        print("Entry must be number! Try again")
        main()


main()
