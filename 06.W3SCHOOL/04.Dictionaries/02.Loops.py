mountainDict = {"mountain": "Hemus", "peak": "Botev", "summit": "2376"}

# Print all keys
for i in mountainDict:
    print(i)

for i in mountainDict.keys():
    print(i)

# Print all values
for x in mountainDict:
    print(mountainDict[x])


for x in mountainDict.values():
    print(x)

# Print keys and values
for y in mountainDict.items():
    print(y)

copyOne = mountainDict.copy()
copyTwo = dict(mountainDict)
print(copyOne)
print(copyTwo)