length = int(input())
matrix = []
primary_elements = []
secondary_elements = []

for i in range(length):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

for row in range(length):
    primary_elements.append(matrix[row][row])
    secondary_elements.append(matrix[row][length - 1 - row])

print(F"Primary diagonal: {', '.join([str(x) for x in primary_elements])}. Sum: {sum(primary_elements)}")
print(F"Secondary diagonal: {', '.join([str(x) for x in secondary_elements])}. Sum: {sum(secondary_elements)}")
