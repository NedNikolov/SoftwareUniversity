import math

year = input()
holidays = int(input())
weekends = int(input())

result = (((48 - weekends) * 3) / 4) + weekends
result += (holidays * 2) / 3

if year == 'leap':
    result += (result * 0.15)

print(f'{math.floor(result):.0f}')

