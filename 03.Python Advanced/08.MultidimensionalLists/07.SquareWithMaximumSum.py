rows, columns = [int(x) for x in input().split(', ')]
matrix = []
sum_matrix = [[0, 0], [0, 0]]
result_index = 0
for row in range(rows):
    nums = [int(x) for x in input().split(', ')]
    matrix.append(nums)

for row in range(rows - 1):
    for col in range(columns - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > result_index:
            result_index = current_sum
            sum_matrix[0][0] = matrix[row][col]
            sum_matrix[0][1] = matrix[row][col + 1]
            sum_matrix[1][0] = matrix[row + 1][col]
            sum_matrix[1][1] = matrix[row + 1][col + 1]

for i in range(len(sum_matrix)):
    for j in range(len(sum_matrix[i])):
        print(sum_matrix[i][j], end=" ")
    print()

print(result_index)
