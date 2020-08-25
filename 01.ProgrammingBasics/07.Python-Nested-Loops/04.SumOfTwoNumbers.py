begin = int(input())
end = int(input())
num = int(input())
boolean = True
counter = 0
for i in range(begin, end + 1):
    for j in range(begin, end + 1):
        counter += 1
        if i + j == num:
            print(f'Combination N:{counter} ({i} + {j} = {i + j})')
            boolean = False
            break
    if not boolean:
        break
if boolean:
    print(f'{counter} combinations - neither equals {num}')
