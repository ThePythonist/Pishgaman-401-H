tedad = int(input("How many number do you need : "))
numbers = []

for i in range(tedad):
    numbers.append(int(input("Enter a number : ")))

print(max(numbers))
print(min(numbers))
