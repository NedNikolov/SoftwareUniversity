n = int(input())
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += int(input())
    else:
        odd += int(input())

if even == odd:
    print('Yes')
    print(f'Sum = {even}')
else:
    print('No')
    print(f'Diff = {abs(even - odd)}')
