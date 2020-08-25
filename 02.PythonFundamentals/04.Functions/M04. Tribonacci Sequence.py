def tribonacci_sequence(num):
    n1 = 0
    n2 = 0
    n3 = 1
    seq = [n3]
    for _ in range(num - 1):
        n1, n2, n3 = n2, n3, n1+n2+n3
        seq.append(n3)
    return seq


nums = int(input())
print(" ".join(list(map(str, tribonacci_sequence(nums)))))
