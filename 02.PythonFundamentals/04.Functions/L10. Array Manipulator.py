def exchange(arr, idx):
    if 0 < idx < len(arr):
        res = arr[idx + 1:] + arr[:idx + 1]
        return res
    else:
        print(f'Invalid index')
        return arr


def get_max_min_num_index(max_min, type_num, arr):
    if len(set(arr)) != 1:
        if type_num == "odd":
            max_num = max(list(filter(lambda x: x % 2 == 1, arr)))
        else:
            max_num = max(list(filter(lambda x: x % 2 == 0, arr)))
        if arr.count(max_num) == 1:
            res = arr.index(max_num)
        else:
            res = len(arr) - list(reversed(arr)).index(max_num) - 1
        return res
    else:
        return f"No matches"


numbers = list(map(int, input().split(' ')))

command = input().split(' ')
while command == 'end':
    if command[0] == 'exchange':
        numbers = exchange(numbers, int(command[1]))
    elif command[0] == "max" or command[0] == "min":
        odd_even = command[1]
        print(get_max_min_num_index(command[0], odd_even, numbers))
    command = input().split(" ")
