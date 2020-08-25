name = input()
n = 0
total = 0
failed = 0

while n != 12 and failed < 2:
    evaluation = float(input())
    if evaluation >= 4.00:
        total += evaluation
        n += 1
    else:
        failed += 1
if failed > 1:
    print(f'{name} has been excluded at {n + 1} grade')
else:
    print(f'{name} graduated. Average grade: {(total / 12):.2f}')
