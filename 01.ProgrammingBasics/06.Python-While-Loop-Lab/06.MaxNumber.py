import sys

n = int(input())
max_num = -sys.maxsize

while n != 0:
    number = int(input())
    if number > max_num:
        max_num = number
    n -= 1
print(max_num)
