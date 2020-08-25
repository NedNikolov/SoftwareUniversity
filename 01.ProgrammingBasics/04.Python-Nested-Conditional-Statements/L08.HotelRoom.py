month = input()
nights = int(input())
studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = nights * 50
    apartment = nights * 65
    if 7 < nights <= 13:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.7
elif month == 'June' or month == 'September':
    studio = nights * 75.20
    apartment = nights * 68.70
    if nights > 14:
        studio *= 0.8
else:
    studio = nights * 76
    apartment = nights * 77

if nights > 14:
    apartment *= 0.90

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')



