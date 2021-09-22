from collections import deque
names = deque()
litters = int(input())

while True:
    name = input()
    if name != 'Start':
        names.append(name)
    else:
        break

command = input()

while command != "End":
    if 'refill' in command:
        litter2 = list(command.split(" "))
        litters += int(litter2[1])
    else:
        litter = int(command)
        if litter <= litters:
            litters -= litter
            print(f"{names.popleft()} got water")
        else:
            print(f"{names.popleft()} must wait")
    command = input()
print(f"{litters} liters left")