scores = {
    "riazi": 17,
    "farsi": 14,
    "fizik": 16,
    "arabi": 10,
    "shimi": 7,
    "amar": 20
}

for k, v in scores.items():
    if v >= 10:
        print(k, "Passed")
    else:
        print(k, "Failed")

moadel = sum(scores.values()) / len(scores)
print(moadel)
