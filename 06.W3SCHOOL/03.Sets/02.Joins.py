fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
tropical = {"pineapple", "papaya", "kiwi"}

allfruits = fruits.union(tropical)
print(allfruits)

fruits.update(tropical)
print(fruits)
fruits.clear()
tropical.clear()

# Keep ONLY the Duplicates
fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
tropical = {"pineapple", "papaya", "kiwi"}

samefruits = fruits.intersection(tropical)
fruits.intersection_update(tropical)

print(fruits)
print(samefruits)

fruits.clear()
tropical.clear()

# Keep All, But NOT the Duplicates
fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
tropical = {"pineapple", "papaya", "kiwi"}

fruits.symmetric_difference_update(tropical)
print(fruits)
