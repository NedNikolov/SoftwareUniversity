from collections import deque


def to_print(bombs, bomb_effects, bomb_casing):
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects) if bomb_effects else 'empty'}")
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing) if bomb_casing else 'empty'}")
    print(f'''Cherry Bombs: {bombs['Cherry Bombs']}
Datura Bombs: {bombs['Datura Bombs']}
Smoke Decoy Bombs: {bombs['Smoke Decoy Bombs']}
''')


def are_bombs_enough(bombs):
    return bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3


bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

effect = [int(x) for x in input().split(',')]
casing = [int(x) for x in input().split(',')]

bomb_effects = deque([x for x in effect])  # deque
bomb_casing = [x for x in casing]  # stack

while bomb_effects and bomb_casing and not are_bombs_enough(bombs):
    first_effect = bomb_effects.popleft()
    first_casing = bomb_casing.pop()
    sum_bombs = first_effect + first_casing
    if sum_bombs == 40:
        bombs['Datura Bombs'] += 1
    elif sum_bombs == 60:
        bombs['Cherry Bombs'] += 1
    elif sum_bombs == 120:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        first_casing -= 5
        if first_casing >= 0:
            bomb_effects.appendleft(first_effect)
            bomb_casing.append(first_casing)

if are_bombs_enough(bombs):
    print(f"Bene! You have successfully filled the bomb pouch!")
    to_print(bombs, bomb_effects, bomb_casing)
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
    to_print(bombs, bomb_effects, bomb_casing)
