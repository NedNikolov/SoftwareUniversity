import math

party_size = int(input())
days = int(input())
result = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
        result -= party_size * 2
    result += 50 - (party_size * 2)
    if i % 3 == 0:
        result -= party_size * 3
    if i % 5 == 0:
        result += party_size * 20
print(f'{party_size} companions received {math.floor(result / party_size):.0f} coins each.')
