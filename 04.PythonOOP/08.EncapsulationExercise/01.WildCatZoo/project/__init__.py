# file = """worker""".split("\n")
#
# for file in file:
#     file = file + ".py"
#     open(file, "a").close()
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo

tiger = Tiger('Panzer', 'male', 2)
zoo = Zoo('5-th', 100, 5, 5)

print(zoo.add_animal(tiger, 99))
vet = Vet('Petar', 29, 5000)
print(zoo.hire_worker(vet))
print(zoo.fire_worker('Gosho'))
print(zoo.fire_worker('Petar'))
