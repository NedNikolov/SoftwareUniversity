rows, cols = [int(x) for x in input().split(' ')]
matrix = [[0 for i in range(cols) ] for j in range(rows)]
a = "a"
b = "a"
c = "a"

for row in range(rows):
    for col in range(cols):
        result = b + a + b
        matrix[row][col] = result
        a = chr(ord(a) + 1)
    a = chr(ord(c) + 1)
    c = chr(ord(c) + 1)
    b = chr(ord(b) + 1)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
