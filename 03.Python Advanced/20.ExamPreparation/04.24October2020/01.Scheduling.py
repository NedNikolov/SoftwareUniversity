from collections import deque

tasks = [int(x) for x in input().split(', ')]
searched_index = int(input())

cycle = deque(sorted([(tasks[index], index) for index in range(len(tasks))]))
result = 0

while cycle:
    number, index = cycle.popleft()
    result += number
    if index == searched_index:
        print(result)
        break
