# import sys
# from io import StringIO
#
# test_input = '-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'
# sys.stdin = StringIO(test_input)

# numbers = [float(x) for x in input().split(' ')]
numbers = tuple(map(float, input().split()))

nums_and_occurances = {}
for num in numbers:
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0
    nums_and_occurances[num] += 1

[print(f"{key} - {value} times") for key, value in nums_and_occurances.items()]

# numbers = tuple(map(float, input().split()))
#
# nums_and_occurances = []
# for num in numbers:
#     if num not in nums_and_occurances:
#         print(f"{num} - {numbers.count(num)} times")
#     nums_and_occurances.append(num)

