from collections import deque


def to_print(gifts_list, wedding_presents, genie_magic_levels):
    if wedding_presents:
        print(f"Materials left: {', '.join(str(x) for x in wedding_presents)}")
    if genie_magic_levels:
        print(f"Magic left: {', '.join(str(x) for x in genie_magic_levels)}")
    if gifts_list['Diamond Jewellery'] > 0:
        print(f"Diamond Jewellery: {gifts_list['Diamond Jewellery']}")
    if gifts_list['Gemstone'] > 0:
        print(f"Gemstone: {gifts_list['Gemstone']}")
    if gifts_list['Gold'] > 0:
        print(f"Gold: {gifts_list['Gold']}")
    if gifts_list['Porcelain Sculpture'] > 0:
        print(f"Porcelain Sculpture: {gifts_list['Porcelain Sculpture']}")



def are_gifts_enough(gifts_list):
    return (gifts_list['Gemstone'] >= 1 and gifts_list['Porcelain Sculpture'] >= 1) or (gifts_list['Gold'] >= 1 and gifts_list['Diamond Jewellery'] >= 1)


def sum_in_range(sum_present):
    if 100 <= sum_present <= 199:
        gifts_list['Gemstone'] += 1
        return True
    elif 200 <= sum_present <= 299:
        gifts_list['Porcelain Sculpture'] += 1
        return True
    elif 300 <= sum_present <= 399:
        gifts_list['Gold'] += 1
        return True
    elif 400 <= sum_present <= 499:
        gifts_list['Diamond Jewellery'] += 1
        return True
    return False


gifts_list = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

materials = [int(x) for x in input().split(' ')]
magics = [int(x) for x in input().split(' ')]

wedding_presents = [x for x in materials]  # deque
genie_magic_levels = deque([x for x in magics])  # stack
gifts = 0

while wedding_presents and genie_magic_levels:
    is_second = False
    material = wedding_presents.pop()
    magic = genie_magic_levels.popleft()
    sum_present = material + magic
    if sum_present < 100:
        if sum_present % 2 == 0:
            material *= 2
            magic *= 3
            sum_present = material + magic
            if sum_in_range(sum_present):
                continue
        else:
            sum_present *= 2
            if sum_in_range(sum_present):
                continue
    elif sum_present >= 500:
        sum_present /= 2
        if sum_in_range(sum_present):
            continue
    else:
        sum_in_range(sum_present)

if are_gifts_enough(gifts_list):
    print(f"The wedding presents are made!")
    to_print(gifts_list, wedding_presents, genie_magic_levels)
else:
    print(f"Aladdin does not have enough wedding presents.")
    to_print(gifts_list, wedding_presents, genie_magic_levels)
