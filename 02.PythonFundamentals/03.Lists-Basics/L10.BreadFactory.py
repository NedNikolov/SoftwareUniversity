orders = input().split('|')
energy = 100
coins = 100
gained_energy = 0
win = True
for i in range(len(orders)):
    order = orders[i].split('-')
    command = order[0]
    value = int(order[1])
    if command == 'rest':
        curr_energy = energy
        energy += value
        if energy > 100:
            gained_energy = 100 - curr_energy
            print(f'You gained {gained_energy} energy.')
            energy = 100
        else:
            print(f'You gained {value} energy.')
        print(f'Current energy: {energy}.')
    elif command == 'order':
        if energy < 30:
            energy += 50
            print('You had to rest!')
        else:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
    else:
        if value < coins:
            coins -= value
            print(f'You bought {command}.')
        else:
            print(f'Closed! Cannot afford {command}.')
            win = False
            break
    if not win:
        break
if win:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
