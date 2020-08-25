hour = int(input())
minute = int(input())

if minute >= 45:
    if hour == 23:
        hour = 0
    else:
        hour += 1

if minute <= 44:
    minute += 15
else:
    minute = (minute + 15) % 60

if minute < 10:
    print(f'{hour}:0{minute}')
else:
    print(f'{hour}:{minute}')
