width = int(input())
length = int(input())
length *= width
command = input()
result = int(command)
while length >= result:
    command = input()
    if command == 'STOP':
        break
    result += int(command)

if command == 'STOP' and length >= result:
    print(f'{length - result} pieces are left.')
else:
    print(f'No more cake left! You need {result - length} pieces more.')

