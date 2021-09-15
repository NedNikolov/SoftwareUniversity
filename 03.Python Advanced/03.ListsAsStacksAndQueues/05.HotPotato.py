from collections import deque
name_kids = input().split(" ")
toss = int(input())
children = deque(name_kids)
i = 1

while len(children) > 1:
    kid = children.popleft()

    if i == toss:
        print(f"Removed {kid}")
        i = 0
    else:
        children.append(kid)
    i += 1

print(f"Last is {children.pop()}")
