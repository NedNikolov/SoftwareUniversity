n = int(input())
word = input()
strings = []
for i in range(n):
    input_text = input()
    strings.append(input_text)
print(strings)
for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)
