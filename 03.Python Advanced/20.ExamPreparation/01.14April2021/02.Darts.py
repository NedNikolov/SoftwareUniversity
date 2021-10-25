def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


player_names = [x for x in input().split(',')]
size = 7
matrix = [input().split(' ') for _ in range(size)]

player_one = [player_names[0], 501, 0]
player_two = [player_names[1], 501, 0]

while True:
    command = input()
    row, col = [int(x) for x in command[1:-1].split(', ')]
    if is_outside(row, col, size):
        player_one[2] += 1
        player_one, player_two = player_two, player_one
        continue

    value = matrix[row][col]
    if value == 'B':
        player_one[2] += 1
        break
    if value == 'T':
        player_one[1] = player_one[1] - ((int(matrix[row][0]) + int(matrix[row][-1]) + \
                                          int(matrix[0][col]) + int(matrix[-1][col])) * 3)
    elif value == 'D':
        player_one[1] = player_one[1] - ((int(matrix[row][0]) + int(matrix[row][-1]) + \
                                          int(matrix[0][col]) + int(matrix[-1][col])) * 2)
    else:
        player_one[1] -= int(matrix[row][col])

    player_one[2] += 1

    if player_one[1] <= 0:
        break
    player_one, player_two = player_two, player_one

print(f"{player_one[0]} won the game with {player_one[2]} throws!")

print(type(player_one))