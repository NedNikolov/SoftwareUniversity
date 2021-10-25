def is_inside(r, c, length):
    if 0 <= r < length and 0 <= c < length:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    return r, c + 1


size = int(input())
matrix = [[0 for j in range(size)] for i in range(size)]
snake_row, snake_col = 0, 0
food_quantity = 0
is_won = True
is_found = False

for row in range(size):
    elements = input()
    for col in range(size):
        element = elements[col]
        if element == 'S':
            snake_row, snake_col = row, col
        matrix[row][col] = element

while food_quantity < 10:
    command = input()
    next_snake_row, next_snake_col = get_next_position(command, snake_row, snake_col)
    matrix[snake_row][snake_col] = '.'
    if is_inside(next_snake_row, next_snake_col, size):
        if matrix[next_snake_row][next_snake_col] == '*':
            food_quantity += 1
        elif matrix[next_snake_row][next_snake_col] == 'B':
            matrix[next_snake_row][next_snake_col] = '.'
            for row in range(size):
                for col in range(size):
                    if matrix[row][col] == 'B':
                        next_snake_row, next_snake_col = row, col
                        is_found = True
                        break
                    if is_found:
                        break
        matrix[next_snake_row][next_snake_col] = 'S'
        snake_row, snake_col = next_snake_row, next_snake_col
    else:

        is_won = False
        break

if is_won:
    print(f"You won! You fed the snake.")
    print(f"Food eaten: {food_quantity}")
else:
    print(f"Game over!")
    print(f"Food eaten: {food_quantity}")
for i in matrix:
    print(''.join(str(x) for x in i))

# size = 4
# matrix = [[0 for j in range(size)] for i in range(size)]
#
# matrix[0][0] = 1
# matrix[0][1] = 2
# matrix[0][2] = 3
# matrix[0][3] = 4
# matrix[1][0] = 5
#
# n = int(input())  # 2. Snake
# s = []
# b = []
# matrix = []
# for j in range(n):
#     row = list(input())
#     matrix.append(row)
#     if 'S' in row:
#         s.append([j, row.index('S')])
#     if 'B' in row:
#         b.append([j, row.index('B')])
# moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
# food = 0
# while True:
#     move = input()
#     next_row = s[0][0] + moves[move][0]
#     next_col = s[0][1] + moves[move][1]
#     matrix[s[0][0]][s[0][1]] = '.'
#     if 0 <= next_row < n and 0 <= next_col < n:
#         if matrix[next_row][next_col] == '*':
#             food += 1
#             matrix[next_row][next_col] = 'S'
#             s = [[next_row, next_col]]
#             if food >= 10:
#                 print("You won! You fed the snake.")
#                 break
#         elif matrix[next_row][next_col] == 'B':
#             if matrix[next_row][next_col] == matrix[b[0][0]][b[0][1]]:
#                 matrix[b[1][0]][b[1][1]] = 'S'
#                 s = [[b[1][0], b[1][1]]]
#             else:
#                 matrix[b[0][0]][b[0][1]] = 'S'
#                 s = [[b[0][0], b[0][1]]]
#             matrix[next_row][next_col] = '.'
#         else:
#             matrix[next_row][next_col] = 'S'
#             s = [[next_row, next_col]]
#     else:
#         print('Game over!')
#         break
# print(f'Food eaten: {food}')
# print('\n'.join(''.join(i) for i in matrix))
