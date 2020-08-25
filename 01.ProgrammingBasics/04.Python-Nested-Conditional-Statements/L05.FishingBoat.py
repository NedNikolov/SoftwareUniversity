budget = float(input())
season = input()
fishermen = int(input())
result = 0

if season == 'Spring':
    result += 3000
elif season == 'Summer':
    result += 4200
elif season == 'Autumn':
    result += 4200
elif season == 'Winter':
    result += 2600

if fishermen <= 6:
    result -= result * 0.10
elif 7 <= fishermen <= 11:
    result -= result * 0.15
elif fishermen >= 12:
    result -= result * 0.25

if fishermen % 2 == 0 and not season == 'Autumn':
    result -= result * 0.05

if budget >= result:
    print(f"Yes! You have {(budget - result):.2f} leva left.")
else:
    print(f"Not enough money! You need {(result - budget):.2f} leva.")
