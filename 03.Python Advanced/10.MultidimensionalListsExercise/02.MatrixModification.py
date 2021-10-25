n = int(input())
matrix = []

for row in range(n):
    rows = [int(x) for x in input().split(' ')]
    matrix.append(rows)


while True:
    command = input().split()
    if command[0] == "END":
        break
    row, col, num = [int(x) for x in command[1:]]
    if command[0] == "Add" and n - 1 >= row >= 0 and n - 1 >= col >= 0:
        matrix[row][col] += num
    elif command[0] == "Subtract" and n - 1 >= row >= 0 and n - 1 >= col >= 0:
        matrix[row][col] -= num
    else:
        print("Invalid coordinates")
for i in matrix:
    print(" ".join(str(x) for x in i))
