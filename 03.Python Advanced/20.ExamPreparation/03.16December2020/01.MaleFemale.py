from collections import deque

m = [int(x) for x in input().split(' ')]
f = [int(x) for x in input().split(' ')]

male_stack = [x for x in m if x > 0]
female_deque = deque([x for x in f if x > 0])
matcher = 0

while male_stack and female_deque:
    male = male_stack.pop()
    female = female_deque.popleft()

    if male % 25 == 0:
        male_stack.pop()
        female_deque.appendleft(female)
        continue
    if female % 25 == 0:
        female_deque.popleft()
        male_stack.append(male)
        continue
    if male == female:
        matcher += 1
    else:
        if male > 2:
            male_stack.append(male - 2)

print(f"Matches: {matcher}")
if not male_stack:
    print(f"Males left: none")
else:
    male_stack.reverse()
    print(f"Males left: {', '.join(str(x) for x in male_stack)}")
if not female_deque:
    print(f"Females left: none")
else:
    print(f"Females left: {', '.join(str(x) for x in female_deque)}")
