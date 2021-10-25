def shopping_list(money, **kwargs):
    curr_money = money
    bought_stuffs = []
    i, j = 0, 1
    backet = 0
    if money < 100:
        return "You do not have enough budget."
    for key, value in kwargs.items():
        product_tem = float(value[i])
        money_item = int(value[j])
        sum_quantity = product_tem * money_item
        if sum_quantity <= curr_money and backet < 5:
            bought_stuffs.append(f"You bought {key} for {sum_quantity:.2f} leva.")
            curr_money -= sum_quantity
            backet += 1
    return "\n".join(bought_stuffs)


print(shopping_list(100,microwave=(70, 2),skirts=(15, 4),coffee=(1.50, 10),))
print(shopping_list(20,jeans=(19.99, 1),))
print(shopping_list(104,cola=(1.20, 2),candies=(0.25, 15),bread=(1.80, 1),pie=(10.50, 5),tomatoes=(4.20, 1),milk=(2.50, 2),juice=(2, 3),eggs=(3, 1),))
