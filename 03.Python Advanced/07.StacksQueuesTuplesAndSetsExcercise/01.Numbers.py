first = set(int(x) for x in input().split(' '))
second = set(int(y) for y in input().split(' '))
n = int(input())

for _ in range(n):
    command = input().split(' ')
    if command[0] == "Add":
        if command[1] == 'First':
            [first.add(int(x)) for x in command[2:]]
        else:
            [second.add(int(x)) for x in command[2:]]
    elif command[0] == "Remove":
        work_set = set([int(x) for x in command[2:]])
        if command[1] == 'First':
            first = first.difference(work_set)
        else:
            second = second.difference(work_set)
    else:
        print(first.issubset(second) or second.issubset(first))

print(', '.join([str(x) for x in sorted(first)]))
print(', '.join([str(x) for x in sorted(second)]))
