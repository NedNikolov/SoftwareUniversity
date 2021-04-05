fruits = ["apple", "banana", "cherry", "orange", "kiwi", "peach"]
result = []

for i in range(len(fruits)):
    if 'a' in fruits[i]:
        result.append(fruits[i])

print(result)

compresultOne = [x for x in fruits if 'a' in x]
compresultTwo = [x for x in fruits if x != 'apple']
print(compresultOne)
print(compresultTwo)

numbers = [x for x in range(10) if x < 5]
print(numbers)
