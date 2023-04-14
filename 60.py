word = "Engineer"

# d = {}
# for i in range(len(word)):
#     d.setdefault(i, word[i])

d = dict(zip(range(len(word)), word))
print(d)
