count = int(input())
salary = float(input())

for i in range(0, count):
    site = input()
    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50

if salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{salary:.0f}')
