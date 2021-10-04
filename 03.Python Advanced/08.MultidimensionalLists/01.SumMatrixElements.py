(n, m) = [int(x) for x in input().split(', ')]

matrix = []
result = 0
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    result += sum(row)
    matrix.append(row)

print(result)
print(matrix)
