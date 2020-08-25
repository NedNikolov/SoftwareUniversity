# The final price is: 3369.71 lv.
# The discount is: 739.69 lv.

sq_metres = float(input())
result = sq_metres * 7.61
discount = result * 0.18
final_price = result - discount

print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')
