numbers = [1, 20, 15, 5]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort(key=str.lower)
print(fruits)
fruitstest = fruits
fruittwo = fruits.copy() #or fruittwo = list(fruits)
print(fruitstest)
print(fruittwo)

fruits.reverse()
print(fruits)
print(fruitstest)
print(fruittwo)
