def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


size = 6
shots = 3
matrix = []
bucket = ""
final_score = 0
is_won = True

for row in range(size):
    elements = input().split(' ')
    matrix.append(elements)

for _ in range(shots):
    line = input().split(', ')
    row = str(line[0])
    row = int(row[1:])
    col = str(line[1])
    col = int(col[:-1])
    if is_inside(row, col, 6):
        bucket = matrix[row][col]
    else:
        continue
    if bucket == 'B':
        matrix[row][col] = "0"
        for s in range(size):
            if matrix[s][col].isdigit():
                final_score += int(matrix[s][col])
    else:
        continue

prises = ['Football', 'Teddy Bear', 'Lego Construction Set']
if final_score < 100:
    print(f"Sorry! You need {100 - final_score} points more to win a prize.")
elif 100 <= final_score <= 199:
    print(f"Good job! You scored {final_score} points, and you've won {prises[0]}.")
elif 200 <= final_score <= 299:
    print(f"Good job! You scored {final_score} points, and you've won {prises[1]}.")
elif final_score >= 300:
    print(f"Good job! You scored {final_score} points, and you've won {prises[2]}.")

