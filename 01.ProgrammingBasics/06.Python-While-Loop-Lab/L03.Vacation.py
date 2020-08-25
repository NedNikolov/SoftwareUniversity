vacation_money = float(input())
current_money = float(input())
days_counter = 0
spending_counter = 0

while current_money < vacation_money and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == 'save':
        current_money += money
        spending_counter = 0
    elif command == 'spend':
        current_money -= money
        spending_counter += 1
        if current_money < 0:
            current_money = 0
if spending_counter == 5:
    print('You can\'t save the money.')
    print(days_counter)
if current_money >= vacation_money:
    print(f'You saved the money for {days_counter} days.')
