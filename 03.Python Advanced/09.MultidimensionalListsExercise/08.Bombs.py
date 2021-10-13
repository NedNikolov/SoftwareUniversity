size = int(input())
matrix = []

for row in range(size):
    rows = [int(x) for x in input().split(" ")]
    matrix.append(rows)

bombs = input().split(" ")

for b in range(len(bombs)):
    bomb_row, bomb_col = map(int, bombs[b].split(','))
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    for rows in range(3):
        for cols in range(3):
            row = bomb_row + rows - 1
            col = bomb_col + cols - 1
            if 0 <= row < len(matrix) and 0 <= col < len(matrix):
                if matrix[row][col] == matrix[bomb_row][bomb_col]:
                    continue
                if matrix[row][col] > 0:
                    matrix[row][col] -= matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

alive_sells = 0
sum = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] > 0:
            alive_sells += 1
            sum += matrix[row][col]

print(f"Alive cells: {alive_sells}")
print(f"Sum: {sum}")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
