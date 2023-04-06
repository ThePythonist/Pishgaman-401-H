numbers = []

for i in range(4):
    numbers.append(int(input("Enter any number : ")))

# numbers.sort()
# print(numbers[::-1])

numbers.sort(reverse=True)
print(numbers)
