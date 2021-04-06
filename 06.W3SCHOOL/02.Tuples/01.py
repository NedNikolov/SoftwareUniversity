# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits)
print(len(fruits))

if 'apple' in fruits:
    print('Yes')
else:
    print('No')

listfruits = list(fruits)
listfruits[5] = "watermelon"
fruits = tuple(listfruits)
print(fruits)

listfruits[7:] = 'orange', 'peach'
fruits = tuple(listfruits)
print(fruits)

listfruits.remove('peach')
# listfruits.pop()
fruits = tuple(listfruits)
print(fruits)

(green, yellow, red, orange, *greenf, orangef) = fruits
print(green)
print(greenf)
print(orange)
print(orangef)

