n = input()
l = list()
for i in range(0, len(n)):
    if n[i].istitle():
        l.append(i)
print(l)
