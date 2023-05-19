# lines = open("words.txt").readlines()
# five_letters = ""
#
# for line in lines:
#     if len(line) == 6:
#         five_letters += line
#
# open("five_letters.txt", "w").write(five_letters)
# print("Done")

lines = open("words.txt").readlines()
five_letters = []

for line in lines:
    if len(line) == 6:
        five_letters.append(line)

output = "".join(five_letters)
open("five_letters.txt", "w").write(output)
print("Done")
