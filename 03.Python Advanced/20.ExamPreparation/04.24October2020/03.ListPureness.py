from collections import deque


def best_list_pureness(numbers, rotations):
    data = {}
    numbers = deque(numbers)
    for rotation in range(rotations + 1):
        result = sum([index * number for index, number in enumerate(numbers)])
        data.update({rotation: result})
        numbers.appendleft(numbers.pop())
    max_pureness = max(data.values())

    for key, value in data.items():
        if max_pureness == value:
            return f"Best pureness {value} after {key} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test1 = ([7, 9, 2, 5, 3, 4], 3)
result1 = best_list_pureness(*test1)
print(result1)


