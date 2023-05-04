class Person:
    name = "pranav"
    job = "software developer"
    home = "Rajgir"

    def info(self):
        print(f"hi! i am {self.name}, i work as {self.job} and my hometown is {self.home}. ")
    # the 'self' parameter reference to the current instance of the class
    # and is used to access the variables that belong to that class.


a = Person()
a.info()

b = Person()

b.name = "suman"
b.job = "CA"
b.home = "Patna"
b.info()
