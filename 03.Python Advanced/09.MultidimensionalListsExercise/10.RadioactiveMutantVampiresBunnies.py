rows, cols = [int(x) for x in input().split(' ')]
matrix = []

player_row = 0
player_col = 0
bunnies = []

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(cols):
        el = row_elements[col]
        if el == 'P':
            player_row, player_col = row, col
        elif el == 'B':
            bunnies.append([row, col])

