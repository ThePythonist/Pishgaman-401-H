# def prime_status(number=0):
#     divs = [i for i in range(1, number + 1) if number % i == 0]
#     # if len(divs) == 2:
#     #     return True
#     # else:
#     #     return False
#     return True if len(divs) == 2 else False
#
#
# n = int(input("Enter any number : "))
# print(prime_status(n))


def prime_status(number=0):
    divs = [i for i in range(1, number + 1) if number % i == 0]
    # return True if len(divs) == 2 else False
    print(True) if len(divs) == 2 else print(False)


n = int(input("Enter any number : "))
prime_status(n)
