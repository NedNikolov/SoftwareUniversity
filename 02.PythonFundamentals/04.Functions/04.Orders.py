def calculation(product, quantity):
    result = 0
    if product == 'coffee':
        result = quantity * 1.50
    elif product == 'water':
        result = quantity * 1.00
    elif product == 'coke':
        result = quantity * 1.40
    elif product == 'snacks':
        result = quantity * 2.00
    return result


order_product = input()
order_quantity = int(input())
print(f'{calculation(order_product, order_quantity):.2f}')
