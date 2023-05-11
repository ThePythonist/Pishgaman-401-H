def f1(text):
    text = text.split()
    lengths = []

    for i in text:
        lengths.append(len(i))

    longest = max(lengths)

    for i in text:
        if len(i) == longest:
            return i


print(f1("python is a good programming language"))


def f2(text):
    text = text.split()
    text.sort(key=len)
    return text[-1]


print(f2("python is a good programming language"))


def f3(text):
    text = text.split()
    longest = max(text, key=len)

    return longest


print(f3("python is a good programming language"))
