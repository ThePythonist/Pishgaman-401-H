info = {
    "name": "mojtaba",
    "major": "computer science",
    "university": "tehran",
    "score": 17.78,
    "grade": "bachelor"
}

while True:
    entry = input("Search for : ")
    if entry in info.keys():
        print("Found :", info[entry])
        break
    else:
        print("Key not found. Try again")
