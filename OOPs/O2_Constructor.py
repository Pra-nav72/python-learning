class Person:
    def __init__(self, name, occ):  # parameterized constructor
        self.name = name
        self.occ = occ

    def info(self):
        print(f"i am {self.name} and i am a {self.occ}")


a = Person("suman", "developer")  # 3 arguments ---> 'self' is invisible
a.info()

b = Person("pranav", "SDA")
b.info()
