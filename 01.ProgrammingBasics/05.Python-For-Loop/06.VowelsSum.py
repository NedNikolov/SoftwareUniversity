word = input()
sum = 0

for s in range(0, len(word)):
    if word[s] == 'a':
        sum += 1
    elif word[s] == 'e':
        sum += 2
    elif word[s] == 'i':
        sum += 3
    elif word[s] == 'o':
        sum += 4
    elif word[s] == 'u':
        sum += 5
print(sum)
