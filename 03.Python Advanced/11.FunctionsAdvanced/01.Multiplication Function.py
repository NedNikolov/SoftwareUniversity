def multiply(*nums):
    result = 1
    for x in nums:
        result *= x

    return result


print(multiply(1, 2, 3, 5))
