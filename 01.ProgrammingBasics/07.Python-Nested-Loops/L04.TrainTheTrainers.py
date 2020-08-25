number = int(input())
sum = 0
average = 0
final = 0
counter = 0
name = input()
while name != 'Finish':
    for j in range(1, number + 1):
        score = float(input())
        sum += score
    average = sum / number
    final += average
    counter += 1
    print(f'{name} - {average:.2f}.')
    name = input()
    sum = 0
    average = 0
final /= counter
print(f'Student\'s final assessment is {final:.2f}.')
