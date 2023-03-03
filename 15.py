word = input("Enter any word : ")

if word == word[::-1]:
    print("Is a mirror word")
else:
    print("Is not a mirror word")
