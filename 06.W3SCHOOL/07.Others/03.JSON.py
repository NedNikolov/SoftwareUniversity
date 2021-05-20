import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
toPython = json.loads(x)

# the result is a Python dictionary:
print(toPython["age"])

# convert into JSON:
toJson = json.dumps(toPython)

# the result is a JSON string:
print(toJson)



