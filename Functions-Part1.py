def checknumber(x):
    if type(x) in [int, float]:
        print("Okay. Continue")
        return "Number"
    else:
        print("Not okay")
        return "Not Number"


print(checknumber("12.3"))
