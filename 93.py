lines = open("words.txt").readlines()
sub_lst = [line for line in lines if "ing" in line[-4:]]

# for line in lines:
#     # if line[-4:-1] == "ing":
#     if "ing" in line[-4:]:
#         sub_lst.append(line)

print(sub_lst)
