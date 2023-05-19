# lines = open("words.txt").readlines()
# items = [line[:-1] for line in lines]
# print(items)

lines = open("words.txt").read().replace("\n", "")
print(lines)
