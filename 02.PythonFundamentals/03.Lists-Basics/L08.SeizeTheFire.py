presents = input().split('#')
water = int(input())
total_fire = 0
effort = 0
result = list()
for i in range(len(presents)):
    command = presents[i].split(' ')
    fire = int(command[2])
    if command[0] == 'Low' and 1 <= fire <= 50:
        if water >= fire:
            total_fire += fire
            effort += (fire * 0.25)
            water -= fire
            result.append(fire)
    elif command[0] == 'Medium' and 51 <= fire <= 80:
        if water >= fire:
            total_fire += fire
            effort += (fire * 0.25)
            water -= fire
            result.append(fire)
    elif command[0] == 'High' and 81 <= fire <= 125:
        if water >= fire:
            total_fire += fire
            effort += (fire * 0.25)
            water -= fire
            result.append(fire)
print('Cells:')
for j in range(len(result)):
    print(' - ' + str(result[j]))
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
