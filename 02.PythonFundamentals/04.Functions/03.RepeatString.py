def repeat(a, b):
    result = ''
    for i in range(b):
        result += a
    return result


word = input()
counter = int(input())
print(repeat(word, counter))
