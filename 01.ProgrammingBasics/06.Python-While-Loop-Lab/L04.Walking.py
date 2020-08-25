steps_count = 0

while steps_count < 10000:
    steps = input()
    if steps == 'Going home':
        steps_count += int(input())
        break
    steps_count += int(steps)

if steps_count >= 10000:
    print(f'Goal reached! Good job!')
else:
    print(f'{10000 - steps_count} more steps to reach goal.')
