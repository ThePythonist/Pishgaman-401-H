numbers = []

for i in range(4):
    entry = input("Entry : ")

    try:
        entry = float(entry)
        numbers.append(entry)
    except ValueError:
        print("Entry is not a number")

print(numbers)
