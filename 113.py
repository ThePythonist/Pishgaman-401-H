class Person:
    def __init__(self, fn, ln, city, cmp):
        self.firstname = fn
        self.lastname = ln
        self.city = city
        self.workplace = cmp

    def talk(self):
        print(f"""
Hello my name is {self.firstname} {self.lastname}
and I live in {self.city}
and i work at {self.workplace}
              """)


pedram = Person("Pedram", "Azizi", "Yazd", "Sabanet")
arshia = Person("Arshia", "Yar Mohammadi", "Tehran", "SnappFood")
arshia.talk()
# print(pedram.city)
