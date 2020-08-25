clothes = input().split('|')
budget = int(input())
real_budget = budget
new_budget = 0
list_sum = list()
collect_sum = 0
for i in range(len(clothes)):
    cloth = clothes[i].split('->')
    article = cloth[0]
    price = float(cloth[1])
    if price <= budget:
        if article == 'Clothes' and 0 <= price <= 50:
            collect_sum += price * 0.40
            budget -= price
            new_budget += round(price * 1.40, 2)
            list_sum.append(round(price * 1.40, 2))
        elif article == 'Shoes' and 0 <= price <= 35:
            collect_sum += price * 0.40
            budget -= price
            new_budget += round(price * 1.40, 2)
            list_sum.append(round(price * 1.40, 2))
        elif article == 'Accessories' and 0 <= price <= 20.50:
            collect_sum += price * 0.40
            budget -= price
            new_budget += round(price * 1.40, 2)
            list_sum.append(round(price * 1.40, 2))
    else:
        continue
for k in range(len(list_sum)):
    print(f'{list_sum[k]:.2f}', end=" ")
print()
print(f'Profit: {collect_sum:.2f}')
if (new_budget + budget) >= real_budget and (new_budget + budget) >= 150:
    print('Hello, France!')
else:
    print('Time to go.')

#--------------------------

product_and_price = input().split('|')
budget = int(input())
new_list = []
profit = 0
new_budget = 0

for product in product_and_price:
    token = product.split('->')
    item = token[0]
    price = float(token[1])
    if item == "Clothes" and price <= 50 and budget - price >= 0:
        budget -= price
        new_price = round(price * 1.40, 2)
        new_list.append(new_price)
        profit += new_price - price
    elif item == "Shoes" and price <= 35 and budget - price >= 0:
        budget -= price
        new_price = round(price * 1.40, 2)
        new_list.append(new_price)
        profit += new_price - price
    elif item == "Accessories" and price <= 20.50 and budget - price >= 0:
        budget -= price
        new_price = round(price * 1.40, 2)
        new_list.append(new_price)
        profit += new_price - price

for i in new_list:
    print(f"{i:.2f}", end=" ")
print()

new_budget = sum(new_list) + budget
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")