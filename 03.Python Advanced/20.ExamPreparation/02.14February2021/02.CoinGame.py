import math


def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    if direction == 'right':
        return r, c + 1
    return False


size = int(input())
matrix = []
path_matrix = []
player_row, player_col = 0, 0
next_player_row, next_player_col = 0, 0
collected_coins = 0
is_won = True

for row in range(size):
    elements = input().split(' ')
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'P':
            player_row, player_col = row, col

while collected_coins < 100:
    line = input()

    if not get_next_position(line, player_row, player_col):
        continue
    else:
        next_player_row, next_player_col = get_next_position(line, player_row, player_col)
        if not is_outside(next_player_row, next_player_col, size):
            if matrix[next_player_row][next_player_col] == 'X':
                is_won = False
                break
            else:
                path_matrix.append([next_player_row, next_player_col])
                collected_coins += int(matrix[next_player_row][next_player_col])
                player_row, player_col = next_player_row, next_player_col
        else:
            is_won = False
            break

if is_won:
    print(f"You won! You've collected {collected_coins} coins.")
    print(f"Your path:")
    for i in path_matrix:
        print(i)
else:
    collected_coins = math.floor(collected_coins / 2)
    print(f"Game over! You've collected {collected_coins} coins.")
    print(f"Your path:")
    for i in path_matrix:
        print(i)





