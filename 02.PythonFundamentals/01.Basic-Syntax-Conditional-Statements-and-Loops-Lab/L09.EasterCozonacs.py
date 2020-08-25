budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) / 4
result = price_flour + price_eggs + price_milk
cozonacs = 0
eggs = 0
counter = 0

while budget > result:
    budget -= result
    cozonacs += 1
    eggs += 3
    counter += 1
    if counter % 3 == 0:
        eggs -= (cozonacs - 2)
print(f'You made {cozonacs} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.')

