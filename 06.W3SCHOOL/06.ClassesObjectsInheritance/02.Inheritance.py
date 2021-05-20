class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f"First name: {self.fname}\nLast name: {self.lname}")


p = Person("Thomas", "Anderson")
p.print_name()


class Agent(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    def welcome(self):
        print(f"{self.fname} {self.lname}: Welcome, Mr. Anderson.")


a = Agent("Mister", "Smith", 1999)
a.print_name()
a.welcome()
print(a.year)


