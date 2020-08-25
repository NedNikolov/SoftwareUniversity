key = int(input())
lines = int(input())
l = list()
for i in range(0, lines):
    symbol = input()
    symbol = ord(symbol) + key
    l.append(chr(symbol))
print(''.join(i for i in l))
