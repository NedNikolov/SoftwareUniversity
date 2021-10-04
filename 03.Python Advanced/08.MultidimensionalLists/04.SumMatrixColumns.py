n, m = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

rows = len(matrix)
columns = len(matrix[0])
column_sums = [0] * columns

for r in range(rows):
    for c in range(columns):
        value = matrix[r][c]
        column_sums[c] += value

[print(x) for x in column_sums]
