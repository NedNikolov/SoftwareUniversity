import sys

max_num = -sys.maxsize
min_num = sys.maxsize
count = int(input())

for n in range(0, count):
    num = int(input())
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
