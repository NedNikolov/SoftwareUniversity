def get_next_position(direction, r, c, steps):
    if direction == 'up':
        return r - steps, c
    if direction == 'down':
        return r + steps, c
    if direction == 'left':
        return r, c - steps
    return r, c + steps


def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


size = 5
matrix = []
player_row, player_col = 0, 0
targets_count = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'A':
            player_row, player_col = row, col
        elif element == 'x':
            targets_count += 1

n = int(input())

shooting_directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

hit_targets = []
for _ in range(n):
    commands = input().split()
    command = commands[0]
    direction = commands[1]

    if command == 'move':
        steps = int(commands[2])
        next_player_row, next_player_col = get_next_position(direction, player_row, player_col, steps)

        if is_outside(next_player_row, next_player_col, size):
            continue
        if matrix[next_player_row][next_player_col] != '.':
            continue
        matrix[player_row][player_col] = '.'
        matrix[next_player_row][next_player_col] = 'A'
        player_row, player_col = next_player_row, next_player_col
    else:
        bullet_row, bullet_col = get_next_position(direction, player_row, player_col, 1)
        while True:
            if is_outside(bullet_row, bullet_col, size):
                break

            if matrix[bullet_row][bullet_col] == 'x':
                matrix[bullet_row][bullet_col] = '.'
                hit_targets.append([bullet_row, bullet_col])
                break

            bullet_row, bullet_col = get_next_position(direction, bullet_row, bullet_col, 1)
        if len(hit_targets) == targets_count:
            break

if len(hit_targets) == targets_count:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_count - len(hit_targets)} targets left.")

for i in hit_targets:
    print(i)
