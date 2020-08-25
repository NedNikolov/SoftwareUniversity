count = int(input())
total = 0
fee = 1

while fee > 0 and count != 0:
    fee = float(input())
    if fee < 0:
        print(f'Invalid operation!')
    else:
        total += fee
        print(f'Increase: {fee:.2f}')
    count -= 1

print(f'Total: {total:.2f}')

