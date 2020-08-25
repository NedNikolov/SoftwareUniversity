presents = input().split(' ')
command = input().split(' ')
while command[0] != 'No' and command[1] != 'Money':
    if command[0] == 'OutOfStock':
        for i in range(len(presents)):
            if presents[i] == command[1]:
                presents[i] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(presents):
            presents[index] = command[1]
    elif command[0] == 'JustInCase':
        presents[-1] = command[1]
    command = input().split(' ')
final = list()
for j in range(len(presents)):
    if presents[j] != 'None':
        final.append(presents[j])
print(' '.join(final))
