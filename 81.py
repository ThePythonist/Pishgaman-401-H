x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

compare = lambda x, y: x if x > y else y
print(compare(x, y), "Is bigger")
