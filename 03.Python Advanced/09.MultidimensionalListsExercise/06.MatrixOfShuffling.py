row, col = [int(x) for x in input().split(' ')]
matrix = []

for rows in range(row):
    cols = [x for x in input().split(' ')]
    matrix.append(cols)


while True:
    command = input().split(' ')
    if command[0] == "END":
        break
    if command[0] != 'swap' or len(command) != 5 or int(command[1]) > row or int(command[2]) > col or \
            int(command[3]) > row or int(command[4]) > col:
        print("Invalid input!")
    else:
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] \
            = matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print()
