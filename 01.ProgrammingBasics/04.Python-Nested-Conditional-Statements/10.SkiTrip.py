days = int(input())
room_type = input()
comment = input()
days -= 1

if room_type == 'room for one person':
    days *= 18
    if comment == 'positive':
        days += (days * 0.25)
    else:
        days -= (days * 0.10)
elif room_type == 'apartment':
    if days < 10:
        days *= 25
        days -= (days * 0.30)
    elif 10 <= days <= 15:
        days *= 25
        days -= (days * 0.35)
    else:
        days *= 25
        days -= (days * 0.50)

    if comment == 'positive':
        days += (days * 0.25)
    else:
        days -= (days * 0.10)
else:
    if days < 10:
        days *= 35
        days -= (days * 0.10)
    elif 10 <= days <= 15:
        days *= 35
        days -= (days * 0.15)
    else:
        days *= 35
        days -= (days * 0.20)

    if comment == 'positive':
        days += (days * 0.25)
    else:
        days -= (days * 0.10)

print(f'{days:.2f}')
