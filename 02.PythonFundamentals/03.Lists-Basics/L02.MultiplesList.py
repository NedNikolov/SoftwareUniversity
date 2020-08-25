factor = int(input())
counter = int(input())
delimiter = 1
multiply_list = list()
length = 1

while length < counter:
    if delimiter % factor == 0:
        multiply_list.append(int(delimiter))
    length = len(multiply_list)
    delimiter += 1
print(multiply_list)