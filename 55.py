ages = {
    "romina": 21,
    "mohammad": 16,
    "maryam": 27,
    "tara": 20,
    "hamed": 50,
    "taha": 19,
}

maxage = max(ages.values())

for i in ages.items():
    if i[1] == maxage:
        print(i[0], "is the oldest")
