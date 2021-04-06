fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
tropical = {"pineapple", "papaya"}
print(fruits)

fruits.add("peach")
fruits.update(tropical)
print(fruits)

fruits.remove('pineapple')
fruits.discard('pineapple')

for x in fruits:
    print(x)



