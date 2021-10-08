row, col = [int(x) for x in input().split(' ')]
matrix = []

for rows in range(row):
    cols = [x for x in input().split(' ')]
    matrix.append(cols)

command = input().split(' ')
while command[0] != "END":
    if command[0] != 'swap' or int(command[1]) > row or int(command[2]) > col or \
            int(command[3]) > row or int(command[4]) > col:
        print("Invalid input!")
    else:
        swap_one = matrix[int(command[1])][int(command[2])]
        swap_two = matrix[int(command[3])][int(command[4])]
        matrix[int(command[1])][int(command[2])] = swap_two
        matrix[int(command[3])][int(command[4])] = swap_one
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print()
    command = input().split(' ')
