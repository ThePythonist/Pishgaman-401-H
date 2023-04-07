n = int(input("Enter any number  : "))
divisors = [i for i in range(1, n + 1) if n % i == 0]
print("Divisors are :", divisors)

# if divisors == [1, n]:
#     print("The number is prime!")
# else:
#     print("The number is not prime!")

if len(divisors) == 2:
    print("The number is prime!")
else:
    print("The number is not prime!")
