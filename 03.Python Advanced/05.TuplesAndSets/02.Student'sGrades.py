# import sys
# from io import StringIO

def average(values):
    return sum(values) / len(values)


# test_input = '''7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
# '''

# sys.stdin = StringIO(test_input)

count = int(input())
students = {}
for _ in range(count):
    student, grade = input().split(' ')
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for name, grades in students.items():
    average_grade = average(grades)
    grades_str = ' '.join(str(f'{x:.2f}') for x in grades)
    print(f'{name} -> {grades_str} (avg: {average_grade:.2f})')


