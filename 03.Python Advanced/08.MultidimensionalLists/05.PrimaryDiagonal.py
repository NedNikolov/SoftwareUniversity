length = int(input())
matrix = []
result = 0
counter = 0

for i in range(length):
    rows = [int(x) for x in input().split(' ')]
    matrix.append(rows)

for rows in range(len(matrix)):
    result += matrix[rows][counter]
    counter += 1

print(result)
