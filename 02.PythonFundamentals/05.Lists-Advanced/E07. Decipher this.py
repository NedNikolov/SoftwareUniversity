words = input().split(' ')
new_string_list = []

for word in words:
    number = ''
    for ch in word:
        if ch.isdigit():
            number += ch
    new_string = word.replace(number, chr(int(number)))
    st = list(new_string)
    st[1], st[-1] = st[-1], st[1]
    new_string = ''.join(st)
    new_string_list.append(new_string)
print(' '.join(new_string_list))
