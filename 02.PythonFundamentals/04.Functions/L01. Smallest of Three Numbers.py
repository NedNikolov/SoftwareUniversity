def smallest_num(a, b, c):
    result = 0
    if a < b and a < c:
        result = a
    elif b < a and b < c:
        result = b
    else:
        result = c
    return result


num_a = int(input())
num_b = int(input())
num_c = int(input())
print(smallest_num(num_a, num_b, num_c))
