def odd_even(numbers):
    odd = 0
    even = 0
    for i in range(len(numbers)):
        num = int(numbers[i])
        if num % 2 == 0:
            even += num
        else:
            odd += num
    print(f'Odd sum = {odd}, Even sum = {even}')


text = input()
odd_even(text)
