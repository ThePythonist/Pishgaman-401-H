lines = open("words.txt").readlines()
sub_lst = []

for line in lines :
    if line[:3] == "sub":
        sub_lst.append(line)

print(sub_lst)