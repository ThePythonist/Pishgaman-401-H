# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# valed = A()
# farzand = B()
#
# farzand.say_goodbye()
# farzand.say_hello()

class Father:
    def __init__(self, fname, address, job):
        self.familyname = fname
        self.address = address
        self.job = job

    def say_hello(self):
        print("hello from father")


class Child(Father):
    def __init__(self, fname, address, university, job=None):
        super().__init__(fname, address, job)
        self.university = university

    def say_goodbye(self):
        print("hello from child")


pedar = Father("Ahmadi", "Ekbatan, Khiaban Varzesh", "Teacher")
farzand = Child("Ahmadi", "Ekbatan, Khiaban Varzesh", "Sharif", "Engineer")
print(farzand.familyname)
print(farzand.university)
