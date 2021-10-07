length = int(input())
matrix = []
primary = []
secondary = []

for row in range(length):
    rows = [int(x) for x in input().split(' ')]
    matrix.append(rows)

for row in range(length):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][length - 1 - row])

primary_sum = sum(primary)
secondary_sum = sum(secondary)
print(abs(primary_sum - secondary_sum))
