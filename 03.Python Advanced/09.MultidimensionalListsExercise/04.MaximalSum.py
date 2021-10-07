rows, cols = [int(x) for x in input().split(' ')]
matrix = []
sum_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
result_index = 0

for row in range(rows):
    char = [int(x) for x in input().split(' ')]
    matrix.append(char)

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > result_index:
            result_index = current_sum
            sum_matrix[0][0] = matrix[row][col]
            sum_matrix[0][1] = matrix[row][col + 1]
            sum_matrix[0][2] = matrix[row][col + 2]
            sum_matrix[1][0] = matrix[row + 1][col]
            sum_matrix[1][1] = matrix[row + 1][col + 1]
            sum_matrix[1][2] = matrix[row + 1][col + 2]
            sum_matrix[2][0] = matrix[row + 2][col]
            sum_matrix[2][1] = matrix[row + 2][col + 1]
            sum_matrix[2][2] = matrix[row + 2][col + 2]

print(f"Sum = {result_index}")
for i in range(len(sum_matrix)):
    for j in range(len(sum_matrix[i])):
        print(sum_matrix[i][j], end=" ")
    print()
