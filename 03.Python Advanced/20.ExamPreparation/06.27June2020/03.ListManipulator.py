from collections import deque


def list_manipulator(numbers, command, action, *args):
    result = deque(numbers)
    if command == 'add':
        if action == 'beginning':
            result = deque(args) + result
        elif action == 'end':
            result += deque(args)

    elif command == 'remove':
        if action == 'beginning':
            if not args:
                result = deque(numbers[1:])
            else:
                count = int(args[0])
                result = deque(numbers[count:])
        else:
            if not args:
                result = deque(numbers[:-1])
            else:
                count = int(args[0])
                result = deque(numbers[:-count])

    return list(result)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
