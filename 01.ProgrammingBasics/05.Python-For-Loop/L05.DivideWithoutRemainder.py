count = int(input())
p1 = 0
p2 = 0
p3 = 0
counter = 0

for i in range(0, count):
    num = int(input())
    counter += 1
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

print(f'{((p1 / counter) * 100):.2f}%')
print(f'{((p2 / counter) * 100):.2f}%')
print(f'{((p3 / counter) * 100):.2f}%')
