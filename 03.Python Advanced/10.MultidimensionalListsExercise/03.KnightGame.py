def is_inside(matrix, row, col):
    size = len(matrix)
    if row < 0 or col < 0 or row >= size or col >= size:
        return False
    return matrix[row][col] == 'K'


def count_affected_knights(matrix, row, col):
    result = 0
    if is_inside(matrix, row - 2, col - 1):
        result += 1
    if is_inside(matrix, row - 2, col + 1):
        result += 1
    if is_inside(matrix, row + 2, col - 1):
        result += 1
    if is_inside(matrix, row + 2, col + 1):
        result += 1
    if is_inside(matrix, row - 1, col - 2):
        result += 1
    if is_inside(matrix, row - 1, col + 2):
        result += 1
    if is_inside(matrix, row + 1, col - 2):
        result += 1
    if is_inside(matrix, row + 1, col + 2):
        result += 1
    return result


n = int(input())
matrix = []

for row in range(n):
    matrix.append(list(input()))

removed_knights = 0

while True:
    max_count, knight_row, knight_col = 0, 0, 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == '0':
                continue
            count = count_affected_knights(matrix, r, c)
            if count > max_count:
                max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)