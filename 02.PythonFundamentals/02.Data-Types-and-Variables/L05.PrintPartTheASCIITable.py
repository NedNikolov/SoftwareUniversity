start = int(input())
stop = int(input())
l = list()
for i in range(start, stop + 1):
    #print(chr(i), end='')
    l.append(i)
print(' '.join(chr(i) for i in l))
