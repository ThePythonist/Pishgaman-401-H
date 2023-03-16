items = [12, 4, False, 6.7, "Java", 8]

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        print(i)
