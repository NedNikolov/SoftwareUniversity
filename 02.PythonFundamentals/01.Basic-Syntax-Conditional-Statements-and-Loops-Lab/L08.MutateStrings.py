word = input()
trans = input()
l = list(word)

for i in range(0, len(word)):
    if word[i] != trans[i]:
        l[i] = trans[i]
        print("".join(l))
