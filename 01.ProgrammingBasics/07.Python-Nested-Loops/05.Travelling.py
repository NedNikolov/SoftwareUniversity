destination = input()
sum_saving = 0
while destination != 'End':
    price = float(input())
    while price >= sum_saving:
        saving = float(input())
        sum_saving += saving
        if sum_saving >= price:
            print(F'Going to {destination}!')
            destination = input()
            sum_saving = 0
            break

