def sum_numbers(a, b, c):
    result = a + b
    return subtract(result, c)


def subtract(result, c):
    return result - c


num_a = int(input())
num_b = int(input())
num_c = int(input())
print(sum_numbers(num_a, num_b, num_c))
