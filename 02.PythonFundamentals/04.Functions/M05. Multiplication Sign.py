def multiplication(a, b, c):
    mul = a * b * c

    if mul == 0:
        print(f"zero")
    elif mul > 0:
        print(f"positive")
    else:
        print(f"negative")


num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
multiplication(num_1, num_2, num_3)
