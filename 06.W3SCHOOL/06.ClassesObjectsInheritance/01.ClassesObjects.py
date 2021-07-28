class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        print(f"My name is {self.name}. I am {self.age} years old.")


p1 = Person("Andersen", 34)
print(p1.name)
print(p1.age)
p1.person_info()

p1.name = input()
p1.age = input()
p1.person_info()



