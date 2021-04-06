fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "orange")

for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

n = 0
while n < len(fruits):
    print(fruits[n])
    n += 1

print(fruits.count("orange"))
print(fruits.index("orange"))