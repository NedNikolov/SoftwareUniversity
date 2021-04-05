# strings are immutable
a_str = 'Hello World'
print(a_str)  # output will be whole string. Hello World
print(a_str[0])  # output will be first character. H
print(a_str[0:5])  # output will be first five characters. Hello

# sets are mutable
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates will be removed

a = set('abracadabra')
print(a)  # unique letters in a
a.add('z')
print(a)

# frozensets are immutable and new element cannot be added
b = frozenset('asdfagsa')
print(b)
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)

# numbers are four types
int_num = 10  # int value
float_num = 10.2  # float value
complex_num = 3.14j  # complex value
long_num = 1234567  # long value

# list can store different data type
list1 = [123, 'abcd', 10.2, 'd']  # can be an array of any data type or single data type.
list2 = ['hello', 'world']
print(list1)  # will output whole list. [123,'abcd',10.2,'d']
print(list1[0:2])  # will output first two element of list. [123,'abcd']
print(list2 * 2)  # will gave list2 two times. ['hello','world','hello','world']
print(list1 + list2)   # will gave concatenation of both the lists.