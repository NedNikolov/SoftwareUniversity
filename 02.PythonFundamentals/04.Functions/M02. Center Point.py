import math


def closest_point(x1, y1, x2, y2):
    result_one = abs(x1) + abs(y1)
    result_two = abs(x2) + abs(y2)
    if result_one <= result_two:
        print(f'({x1}, {y1})')
    else:
        print(f'({x2}, {y2})')


cx1 = int(input())
cy1 = int(input())
cx2 = int(input())
cy2 = int(input())
closest_point(cx1, cy1, cx2, cy2)
