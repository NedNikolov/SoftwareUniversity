# first_len, second_len = [int(x) for x in input().split(' ')]
first_len, second_len = map(int, input().split(' '))

first_set = {input() for n in range(first_len)}
second_set = {input() for n in range(second_len)}
third_set = first_set.intersection(second_set)

[print(n) for n in third_set]
