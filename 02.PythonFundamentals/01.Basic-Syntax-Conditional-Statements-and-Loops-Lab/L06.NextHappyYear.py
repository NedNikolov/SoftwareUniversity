'''
n = input()
while n[0] == n[1] or n[0] == n[2] or n[0] == n[3] or n[1] == n[2] or n[1] == n[3] or n[3] == n[2]:
    num = int(n) + 1
    n = str(num)
print(n)
'''
number = int(input())

while True:
    number += 1
    year = str(number)
    if len(set(year)) == len(year):
        print(year)
        break
