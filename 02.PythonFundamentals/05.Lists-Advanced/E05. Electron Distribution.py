def atom_shell(n):
    counter = 1
    list = []
    while n:
        result = 2 * counter ** 2
        if n <= result:
            result = n
        list.append(result)
        counter += 1
        n -= result
    print(list)


atom = int(input())
atom_shell(atom)
