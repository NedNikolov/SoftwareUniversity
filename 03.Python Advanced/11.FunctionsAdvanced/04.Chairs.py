def generate_combination(values, index, count, comb):
    if len(comb) == count:
        print(", ".join([str(x) for x in comb]))
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combination(values, i + 1, count, comb)
        comb.pop()


text = list(input().split(', '))
num = int(input())
generate_combination(text, 0, num, [])
