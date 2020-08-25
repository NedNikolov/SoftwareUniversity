projection_type = input()
rows = int(input())
columns = int(input())
result = rows * columns

if projection_type == 'Premiere':
    result *= 12
elif projection_type == 'Normal':
    result *= 7.50
elif projection_type == 'Discount':
    result *= 5

print(f'{result:.2f}')
