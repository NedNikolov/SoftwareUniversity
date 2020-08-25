n = int(input())
matrix = list([])
counter = 0
for i in range(n):
    numbers = list(map(int, input().split(" ")))
    matrix.append(numbers)
attack = input().split(" ")
for j in range(len(attack)):
    cords = attack[j].split('-')
    row = int(cords[0])
    col = int(cords[1])
    if matrix[row][col] > 1:
        matrix[row][col] -= 1
    elif matrix[row][col] == 1:
        matrix[row][col] = 0
        counter += 1
print(counter)
