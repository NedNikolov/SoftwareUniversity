n = int(input())
summ = 0
for i in range(0, n):
    symbol = input()
    summ += ord(symbol)
print(f'The sum equals: {summ}')