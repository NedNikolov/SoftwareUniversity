def factorial_divider(fact, div):
    result_one = 1
    result_two = 1
    for i in range(1, fact + 1):
        result_one = result_one * i
    for j in range(1, div + 1):
        result_two = result_two * j
    result_one /= result_two
    print(f'{result_one:.2f}')


factorial = int(input())
divider = int(input())
factorial_divider(factorial, divider)
