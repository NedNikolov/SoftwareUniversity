length = int(input())
matrix = []

for i in range(length):
    row = [x for x in input()]
    matrix.append(row)

symbol = input()
is_found = False
row, col = None, None

for i in range(length):
    if is_found:
        break
    for j in range(length):
        check = matrix[i][j]
        if symbol == check:
            row, col = i, j
            is_found = True
            break

if is_found:
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")
