x = y = [0, 1, 2]
x[0] = 3
y = [0, 1, 3]

print(x)
print(y)

x = [1, 2, [3, 4, 5], 6, 7]
print(x[2])
print(x[2][1])

i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1

a = 'hello'
print(list(a))  # ['h', 'e', 'l', 'l', 'o']
print(set(a))  # {'o', 'e', 'l', 'h'}
print(tuple(a))  # ('h', 'e', 'l', 'l', 'o')

normal = 'foo\nbar'  # foo
                     # bar
escaped = 'foo\\nbar'  # foo\nbar
raw = r'foo\nbar'  # foo\nbar
print(normal)
print(escaped)
print(raw)

nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][1])

