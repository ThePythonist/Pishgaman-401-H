# def check(word):
#     if len(word) == len(set(word)):
#         print("Tekrari nadarad")
#     else:
#         print("Tekrari darad")

check = lambda word: "Tekrari nadarad" if len(word) == len(set(word)) else "Tekrari darad"
print(check("dad"))
