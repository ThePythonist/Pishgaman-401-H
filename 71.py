def filter(items):
    for i in items :
        if type(i) == int or type(i) == float:
            print(i)

    return "Executed"


lst = ["shatel", 1024, True, 256.6, 12, 16, "Irancell"]
filter(lst)
