command = input()
numbers = [int(x) for x in input().split(' ')]

check = 0 if command == 'Even' else 1
sum = sum(filter(lambda x: x % 2 == check, numbers))
print(sum * len(numbers))
