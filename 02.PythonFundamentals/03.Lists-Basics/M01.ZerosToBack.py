numbers = list(map(int, input().split(', ')))
for i in range(len(numbers)):
    if int(numbers[i]) == 0:
        numbers.pop(i)
        numbers.append(0)
print(numbers)


numbers = list(map(int, input().split(", ")))
zero_list = []
i = 0

while 0 in numbers:
    if numbers[i] == 0:
        numbers.pop(i)
        zero_list.append(0)
    i += 1
numbers += zero_list
print(numbers)
