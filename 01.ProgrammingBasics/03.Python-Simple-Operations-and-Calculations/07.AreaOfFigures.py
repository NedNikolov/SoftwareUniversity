import math

figure = input()

if figure == 'square':
    result = float(input())
    result *= result
    print(f'{result:.3f}')
elif figure == 'circle':
    result = float(input())
    result *=result
    result *= math.pi
    print(f'{result:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    result = a * b
    print(f'{result:.3f}')
else:
    a = float(input())
    b = float(input())
    result = (a * b) / 2
    print(f'{result:.3f}')
