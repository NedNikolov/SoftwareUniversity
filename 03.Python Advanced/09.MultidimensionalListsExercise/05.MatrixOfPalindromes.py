rows, cols = [int(x) for x in input().split(' ')]
matrix = [[0 for i in range(cols) ] for j in range(rows)]

for row in range(rows):
    for col in range(cols):
        print(f'{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}', end=' ')
    print()
