def is_inside(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


directions = {
    "up": (-1, 0),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down": (1, 0),
    "down_left": (1, -1),
    "down_right": (1, 1),
    "left": (0, -1),
    "right": (0, 1),
}

size = 8
matrix = [input().split(' ') for _ in range(size)]
queens = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'Q':
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                while is_in_range(next_row, next_col, size):
                    if matrix[next_row][next_col] == 'Q':
                        break
                    if matrix[next_row][next_col] == 'K':
                        queens.append([row, col])
                        break
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]

if queens:
    for i in queens:
        print(i)
else:
    print(f"The king is safe!")


