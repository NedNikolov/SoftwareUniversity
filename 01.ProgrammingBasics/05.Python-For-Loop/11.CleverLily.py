lily_years = int(input())
wash_price = float(input())
toy_price = float(input())
result = 0
counter = 0
add_sum = 0

for y in range(2, lily_years + 1, 2):
    result += 10 + add_sum
    add_sum += 10
    counter += 1

for t in range(1, lily_years + 1, 2):
    result += toy_price
result -= counter

if wash_price > result:
    print(f'No! {(wash_price - result):.2f}')
else:
    print(f'Yes! {(result - wash_price):.2f}')


