lst = [1, 2, 3, 4, 5]

for i in range(5):
    x = int(input("Enter a number : "))
    if 5 < x < 11:
        lst.append(x)
    else :
        print("The number is not between 6-10")
print(lst)
