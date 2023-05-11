# def factorial(x):
#     if x == 1:
#         return x
#     else:
#         return x * factorial(x - 1)


factorial = lambda x : x if x == 1 else x * factorial(x-1)
print(factorial(5))