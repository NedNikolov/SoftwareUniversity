fruit = input()
week_day = input()
quantity = float(input())
boolean = True

if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or week_day == 'Thursday' or week_day == 'Friday':
    if fruit == 'banana':
        quantity *= 2.50
    elif fruit == 'apple':
        quantity *= 1.20
    elif fruit == 'orange':
        quantity *= 0.85
    elif fruit == 'grapefruit':
        quantity *= 1,45
    elif fruit == 'kiwi':
        quantity *= 2.70
    elif fruit == 'pineapple':
        quantity *= 5.50
    elif fruit == 'grapes':
        quantity *= 3.85
    else:
        boolean = False
elif week_day == 'Saturday' or week_day == 'Sunday':
    if fruit == 'banana':
        quantity *= 2.70
    elif fruit == 'apple':
        quantity *= 1.25
    elif fruit == 'orange':
        quantity *= 0.90
    elif fruit == 'grapefruit':
        quantity *= 1.60
    elif fruit == 'kiwi':
        quantity *= 3.00
    elif fruit == 'pineapple':
        quantity *= 5.60
    elif fruit == 'grapes':
        quantity *= 4.20
    else:
        boolean = False
else:
    boolean = False

if boolean == True:
    print(f'{quantity:.2f}')
else:
    print('error')
