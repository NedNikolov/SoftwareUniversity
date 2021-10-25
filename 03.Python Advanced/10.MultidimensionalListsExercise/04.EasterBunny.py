def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


size = int(input())
matrix = []
bunny_row, bunny_col = 0, 0

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'B':
            bunny_row, bunny_col = row, col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

max_eggs = float('-inf')
best_directions = ''
best_path = []

for direction, step in directions.items():
    eggs = 0
    curr_row, curr_col = bunny_row, bunny_col
    path = []
    while True:
        curr_row, curr_col = step(curr_row, curr_col)
        if not is_inside(curr_row, curr_col, size):
            break
        if matrix[curr_row][curr_col] == 'X':
            break
        eggs += int(matrix[curr_row][curr_col])
        path.append([curr_row, curr_col])
    if eggs > max_eggs:
        max_eggs, best_directions, best_path = eggs, direction, path

print(best_directions)
for i in best_path:
    print(i)
print(max_eggs)
