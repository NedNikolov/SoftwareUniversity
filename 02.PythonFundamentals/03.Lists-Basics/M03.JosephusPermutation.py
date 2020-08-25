def josephus(elements, skip):
    idx = 0
    result = []
    while len(elements) > 0:
        idx = (idx + skip - 1) % len(elements)
        result.append((elements.pop(idx)))

    return result


def trim_white_spaces(elements):
    result = elements
    no_spaces = ''
    for num in result:
        if no_spaces != '':
            no_spaces += ','
        for char in str(num):
            if ord(char) in range(48, 58):
                no_spaces += char

    return '[' + no_spaces + ']'


elements_list = input().split()
k = int(input())

print((trim_white_spaces(josephus(elements_list, k))))


# for i in range(0, len(new_list)):
#     new_list[i] = int(new_list[i])
# print(''.join(new_list))
