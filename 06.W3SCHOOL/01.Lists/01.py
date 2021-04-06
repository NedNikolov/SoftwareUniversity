# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.

# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(fruits))
print(fruits)
print(fruits[-1])
print(fruits[4:])
print(fruits[:4])
print(fruits[-4:-1])
print(fruits[3:-1])
fruits[5] = 'watermelon'
print(fruits[5])
fruits[1:3] = ["raspberry", "strawberry"]
print(fruits)
fruits.append("PEACH")
print(fruits)
fruits.insert(-1, "ORANGE")
print(fruits)

nofruit = ["tomato"]
fruits.extend(nofruit)
print(fruits)
fruits.remove("raspberry")
fruits.pop(1)
fruits.pop()
print(fruits)
fruits.clear()
