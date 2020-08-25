def ascii_symbols(a, b):
    one = ord(a)
    two = ord(b)
    for i in range(one + 1, two, 1):
        print(chr(i), end=' ')


symbol_a = input()
symbol_b = input()
ascii_symbols(symbol_a, symbol_b)
