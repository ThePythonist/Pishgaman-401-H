import random


def generate1():
    password = []

    for i in range(6):
        number = str(random.randint(0, 9))
        password.append(number)

    pswd = "".join(password)
    print(pswd)


# generate1()

def generate2():
    password = ""
    for i in range(6):
        number = str(random.randint(0, 9))
        password += number

    print(password)


generate2()
