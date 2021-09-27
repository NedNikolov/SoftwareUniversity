n = int(input())
parking = set()

for _ in range(n):
    action, dkn = input().split(', ')
    if action == 'IN':
        parking.add(dkn)
    else:
        parking.remove(dkn)

if parking:
    [print(dkn) for dkn in parking]
else:
    print('Parking Lot is Empty')
