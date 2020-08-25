fight_count = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
shield_count = 0
price = 0

for i in range(1, fight_count + 1):
    if i % 2 == 0:
        price += helmet
    if i % 3 == 0:
        price += sword
        if i % 2 == 0:
            price += shield
            shield_count += 1
    if shield_count % 2 == 0 and shield_count > 0:
        price += armor
print(f'Gladiator expenses: {price:.2f} aureus')
