n = input()
numbers = list()
numbers = n.split(" ")
for i in range(len(numbers)):
    if int(numbers[i]) > 0:
        numbers[i] = '-' + numbers[i]
    elif numbers[i] == '0':
        numbers[i] = int(numbers[i])
    else:
        numbers[i] = str(numbers[i][1:])
    numbers[i] = int(numbers[i])
print(numbers)
