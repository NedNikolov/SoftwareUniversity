divisor = int(input())
boundary = int(input())

for i in range(boundary):
    if boundary % divisor == 0 and boundary > 1:
        print(boundary)
        break
    else:
        boundary -= 1
        continue
