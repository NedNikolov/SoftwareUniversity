list_strings = input().split(' ')
list_strings.sort()
list_strings.reverse()
print(''.join(list_strings))

numbers = input().split(" ")
numbers.sort(reverse=True)
print("".join(map(str, numbers)))
