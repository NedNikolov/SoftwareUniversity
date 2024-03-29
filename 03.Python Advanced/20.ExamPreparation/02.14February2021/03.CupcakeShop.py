def stock_availability(inventory, command, *args):
    if command == 'delivery':
        return inventory + list(args)
    else:
        if not args:
            return inventory[1:]
        if isinstance(args[0], int):  # args[0].isdigit() not working, str(args[0]).isdigit() is working
            count = int(args[0])
            return inventory[count:]
        else:
            sold_items = set(args)
            return [item for item in inventory if item not in sold_items]


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
