lines = open("words.txt").read().replace("\n", "")
open("one_line.txt","w").write(lines)
print("Done")