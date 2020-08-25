n = int(input())
numbers = []
filtered = []
for i in range(n):
    curr_num = int(input())
    numbers.append(curr_num)
text = input()
if text == 'even':
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif text == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif text == 'negative':
    for number in numbers:
        if number < 0:
            filtered.append(number)
else:
    for number in numbers:
        if number >= 0:
            filtered.append(number)
print(filtered)
