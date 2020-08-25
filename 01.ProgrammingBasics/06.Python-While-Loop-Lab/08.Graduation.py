name = input()
n = 12
total = 0
while n != 0:
    evaluation = float(input())
    if evaluation >= 4.00:
        total += evaluation
        n -= 1
total /= 12
if total >= 4.00:
    print(f'{name} graduated. Average grade: {total:.2f}')
