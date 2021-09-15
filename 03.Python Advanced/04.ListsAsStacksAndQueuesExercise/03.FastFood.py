from collections import deque
quantity = int(input())
orders = deque(map(int, input().split()))
max_order = max(orders)


while orders:
    current_order = orders[0]
    if current_order > quantity:
        break
    else:
        quantity -= current_order
        orders.popleft()

print(max_order)
if orders:
    print(f"Orders left:", end=" ")
    print(" ".join(map(str, orders)))
else:
    print("Orders complete")
