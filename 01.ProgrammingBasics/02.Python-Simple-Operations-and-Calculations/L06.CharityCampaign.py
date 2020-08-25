campaign_days = float(input())
cookie_makers = float(input())
cakes = float(input())
waffles = float(input())
pancakes = float(input())

day_price = ((cakes * 45) + (waffles * 5.80) + (pancakes * 3.20)) * cookie_makers
day_price *= campaign_days
bills = day_price - (day_price * 0.875)
#bills = day_price - (day_price / 8)
day_price -= bills
print(f'{day_price:.2f}')
