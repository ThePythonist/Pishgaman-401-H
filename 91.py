lines = open("words.txt").readlines()
# lines.sort(key=len)
# maximum = lines[-1]
# print(maximum)
# print(len(maximum))
# -----------------------------
maximum = max(lines, key=len)
# print(maximum)
# print(len(maximum))
# -----------------------------
for line in lines:
    if len(line) == len(maximum):
        print(line)
