number = float(input())
input_one = input()
input_two = input()

if input_one == 'mm':
    if input_two == 'cm':
        number /= 10
        print(f'{number:.3f}')
    else:
        number /= 1000
        print(f'{number:.3f}')
elif input_one == 'cm':
    if input_two == 'mm':
        number *= 10
        print(f'{number:.3f}')
    else:
        number /= 100
        print(f'{number:.3f}')
else:
    if input_two == 'cm':
        number *= 100
        print(f'{number:.3f}')
    else:
        number *= 1000
        print(f'{number:.3f}')
