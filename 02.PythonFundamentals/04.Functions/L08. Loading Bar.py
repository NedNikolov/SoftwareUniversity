def percentage(number):
    if number == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f'{number}% ', end='')
        print('[', end='')
        print('%' * int(number / 10), end='')
        print('.' * int((100 - number) / 10), end='')
        print(']')
        print('Still loading...')


num = int(input())
percentage(num)
