tables = int(input())
length = float(input())
width = float(input())

carpet_result = tables * (length + 2 * 0.30) * (width + 2 * 0.30)
care_area = tables * (length / 2) * (length / 2)
usd = carpet_result * 7 + care_area * 9
bgn = usd * 1.85

print(f'{usd:.2f} USD')
print(f'{bgn:.2f} BGN')
