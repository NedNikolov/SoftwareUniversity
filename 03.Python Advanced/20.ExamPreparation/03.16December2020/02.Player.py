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
    if direction == 'right':
        return r, c + 1
    return False


text = input()
size = int(input())
matrix = [[0 for j in range(size)] for i in range(size)]
player_row, player_col = 0, 0
is_won = True

for row in range(size):
    elements = input()
    for col in range(size):
        element = elements[col]
        if element == 'P':
            player_row, player_col = row, col
        matrix[row][col] = element

turns = int(input())

for turn in range(turns):
    command = input()
    next_player_row, next_player_col = get_next_position(command, player_row,player_col,)
    if not is_inside(next_player_row, next_player_col, size):
        is_won = False
        if text:
            text = text[:-1]
        continue
    elif matrix[next_player_row][next_player_col] != '-':
        text += matrix[next_player_row][next_player_col]
    matrix[player_row][player_col] = '-'
    matrix[next_player_row][next_player_col] = 'P'
    player_row, player_col = next_player_row, next_player_col

print(text)
for i in matrix:
    print(''.join(str(x) for x in i))
