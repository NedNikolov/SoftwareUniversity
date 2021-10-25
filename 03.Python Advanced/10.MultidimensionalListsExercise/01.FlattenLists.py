sublists = input().split("|")
result = []

for sublist in range(len(sublists) - 1, -1, -1):
    elements = sublists[sublist].split()
    result += elements
print(' '.join(result))
