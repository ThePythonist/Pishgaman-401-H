def func(start, end):
    numbers = range(start, end)
    print(*list(numbers))


x, y = int(input("Range start : ")), int(input("Range end : "))
func(x, y)
