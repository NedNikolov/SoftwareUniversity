def operate(operator, *numbers):
    def get_initial_value(operator):
        if operator in ('+', '-'):
            return 0
        else:
            return 1

    result = get_initial_value(operator)

    for x in numbers:
        if operator == '+':
            result += x
        elif operator == '-':
            result -= x
        elif operator == '*':
            result *= x
        else:
            result /= x
    return result


operator = input()
nums = list([int(x) for x in input().split(', ')])
operate(operator, nums)
