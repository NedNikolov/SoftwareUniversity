quantity = int(input())
days = int(input())
budget = 0
totalSpirit = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 10 == 0:
        budget += 23
        totalSpirit -= 20
        if days == i:
            totalSpirit -= 30
    if i % 5 == 0:
        budget += 15 * quantity
        totalSpirit += 17
    if i % 15 == 0:
        totalSpirit += 30
    if i % 3 == 0:
        budget += 8 * quantity
        totalSpirit += 13
    if i % 2 == 0:
        budget += 2 * quantity
        totalSpirit += 5

print(f'Total cost: {budget}')
print(f'Total spirit: {totalSpirit}')
