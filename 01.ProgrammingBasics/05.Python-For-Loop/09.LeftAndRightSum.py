n = int(input())
right = 0
left = 0

for i in range(0, n):
    right += int(input())
for j in range(0, n):
    left += int(input())

if right == left:
    print(f'Yes, sum = {right}')
else:
    print(f'No, diff = {abs(right - left)}')
