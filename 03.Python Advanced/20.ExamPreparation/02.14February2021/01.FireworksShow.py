from collections import deque
# import sys
# from io import StringIO
#
# test_input1 = '''5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
# '''
#
# test_input2 = '''-15, -8, 0, -16, 0, -22
# 10, 5
# '''
#
# sys.stdin = StringIO(test_input2)


def print_fireworks(fireworks, remaining_firework_effects, remaining_explosive_powers):
    if remaining_firework_effects:
        print(f"Firework Effects left: {', '.join(str(x) for x in remaining_firework_effects)}")
    if remaining_explosive_powers:
        print(f"Explosive Power left: {', '.join(str(x) for x in remaining_explosive_powers)}")
    print(f'''Palm Fireworks: {fireworks['palm']}
Willow Fireworks: {fireworks['willow']}
Crossette Fireworks: {fireworks['crossette']}
''')


def print_success(fireworks, remaining_firework_effects, remaining_explosive_powers):
    print(f'Congrats! You made the perfect firework show!')
    print_fireworks(fireworks, remaining_firework_effects, remaining_explosive_powers)



def print_fail(fireworks, remaining_firework_effects, remaining_explosive_powers):
    print("Sorry. You can't make the perfect firework show.")
    print_fireworks(fireworks, remaining_firework_effects, remaining_explosive_powers)


def are_fireworks_enough(fireworks):
    return fireworks['palm'] >= 3 and fireworks['willow'] >= 3 and fireworks['crossette'] >= 3
# return all(x >= 3 for x in fireworks.values())


def mix_fireworks(firework, explosive):
    firework_effects = deque([x for x in firework if x > 0]) # deque
    explosive_powers = [x for x in explosive if x > 0]    # stack

    fireworks = {
        'palm': 0,
        'willow': 0,
        'crossette': 0
    }

    while firework_effects and explosive_powers and not are_fireworks_enough(fireworks):
        firework_effect = firework_effects.popleft()
        explosive_power = explosive_powers.pop()
        current_sum = firework_effect + explosive_power

        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks['crossette'] += 1
        elif current_sum % 3 == 0:
            fireworks['palm'] += 1
        elif current_sum % 5 == 0:
            fireworks['willow'] += 1
        else:
            if firework_effect > 1:
                firework_effects.append(firework_effect - 1)
            explosive_powers.append(explosive_power)
    return fireworks, firework_effects, explosive_powers


fv = [int(x) for x in input().split(',')]
ep = [int(x) for x in input().split(',')]

(fireworks, remaining_firework_effects, remaining_explosive_powers) = mix_fireworks(fv, ep)

if are_fireworks_enough(fireworks):
    print_success(fireworks, remaining_firework_effects, remaining_explosive_powers)
else:
    print_fail(fireworks, remaining_firework_effects, remaining_explosive_powers)

mix_fireworks(fv, ep)
