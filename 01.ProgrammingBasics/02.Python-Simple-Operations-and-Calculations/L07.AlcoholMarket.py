whiskey_price = float(input())
beer = float(input())
wine = float(input())
rakia = float(input())
whiskey = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price - (0.40 * rakia_price)
beer_price = rakia_price - (0.80 * rakia_price)
whiskey_price *= whiskey
beer_price *= beer
wine_price *= wine
rakia_price *= rakia
result = whiskey_price + beer_price + wine_price + rakia_price

print(f'{result:.2f}')





