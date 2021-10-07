rows, cols = [int(x) for x in input().split(' ')]
matrix = []
counter = 0

for row in range(rows):
    char = [x for x in input().split(' ')]
    matrix.append(char)

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            counter += 1

print(counter)
