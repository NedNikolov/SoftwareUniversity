fruits = ["apple", "banana", "cherry", "orange", "kiwi", "peach"]

for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

w = 0
while w < len(fruits):
    print(fruits[w])
    w += 1

[print(x) for x in fruits]
