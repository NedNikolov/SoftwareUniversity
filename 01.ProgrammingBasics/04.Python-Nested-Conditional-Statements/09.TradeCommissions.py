city = input()
sell = float(input())
boolean = False

if city == 'Sofia':
    if sell < 0:
        boolean = True
    elif 0 <= sell <= 500:
        sell *= 0.05
    elif 500 <= sell <= 1000:
        sell *= 0.07
    elif 1000 <= sell <= 10000:
        sell *= 0.08
    else:
        sell *= 0.12
elif city == 'Varna':
    if sell < 0:
        boolean = True
    elif 0 <= sell <= 500:
        sell *= 0.045
    elif 500 <= sell <= 1000:
        sell *= 0.075
    elif 1000 <= sell <= 10000:
        sell *= 0.10
    else:
        sell *= 0.13
elif city == 'Plovdiv':
    if sell < 0:
        boolean = True
    elif 0 <= sell <= 500:
        sell *= 0.055
    elif 500 <= sell <= 1000:
        sell *= 0.08
    elif 1000 <= sell <= 10000:
        sell *= 0.12
    else:
        sell *= 0.145
else:
    boolean = True

if boolean == True:
    print('error')
else:
    print(f'{sell:.2f}')
