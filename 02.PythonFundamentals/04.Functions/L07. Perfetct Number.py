def perfect(number):
    perfect_num = 0
    length = int(number / 2)
    for i in range(1, length + 1):
        if number % i == 0:
            perfect_num += i
    if perfect_num == number:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


num = int(input())
perfect(num)
