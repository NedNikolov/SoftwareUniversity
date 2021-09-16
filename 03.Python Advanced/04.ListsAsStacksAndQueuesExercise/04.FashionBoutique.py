clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_rack = 1
curr_rack_capacity = rack_capacity

while clothes:
    clothing = clothes[-1]
    if clothing > curr_rack_capacity:
        used_rack += 1
        curr_rack_capacity = rack_capacity
    else:
        curr_rack_capacity -= clothing
        clothes.pop()
print(used_rack)
