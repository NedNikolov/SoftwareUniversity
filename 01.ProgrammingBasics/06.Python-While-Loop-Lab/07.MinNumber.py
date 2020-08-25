import sys

n = int(input())
min_num = sys.maxsize

while n != 0:
    number = int(input())
    if number < min_num:
        min_num = number
    n -= 1
print(min_num)
