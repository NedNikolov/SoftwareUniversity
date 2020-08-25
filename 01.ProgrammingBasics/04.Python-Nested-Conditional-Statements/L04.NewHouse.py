flowers_type = input()
flowers_count = int(input())
budget = float(input())
result = 0

if flowers_type == 'Roses':
    result = flowers_count * 5
    if flowers_count > 80:
        result -= (result * 0.10)
elif flowers_type == 'Dahlias':
    result = flowers_count * 3.80
    if flowers_count > 90:
        result -= (result * 0.15)
elif flowers_type == 'Tulips':
    result = flowers_count * 2.80
    if flowers_count > 80:
        result -= (result * 0.15)
elif flowers_type == 'Narcissus':
    result = flowers_count * 3
    if flowers_count < 120:
        result += (result * 0.15)
else:
    result = flowers_count * 2.50
    if flowers_count < 80:
        result += (result * 0.20)

if budget >= result:
    print(f'Hey, you have a great garden with {flowers_count} {flowers_type} and {(budget - result):.2f} leva left.')
else:
    print(f'Not enough money, you need {(result - budget):.2f} leva more.')

