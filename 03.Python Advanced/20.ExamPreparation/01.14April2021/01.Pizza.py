from collections import deque

orders = [int(x) for x in input().split(',')]
employers = [int(x) for x in input().split(',')]
total_pizza = 0

orders_deque = deque([x for x in orders if 0 < x < 11])  # deque
employers_stack = [x for x in employers]  # stack

while orders_deque and employers_stack:
    pizza = orders_deque.popleft()
    worker = employers_stack.pop()
    if pizza <= worker:
        total_pizza += pizza
    if pizza > worker:
        remaining_pizza = pizza - worker
        total_pizza += worker
        orders_deque.appendleft(remaining_pizza)

if employers_stack:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(str(x) for x in employers_stack)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders_deque)}")
