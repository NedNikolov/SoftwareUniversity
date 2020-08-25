length = int(input())
width = int(input())
height = int(input())
percentage_volume = float(input())

result = (length * width * height) * 0.001
percentage_result = percentage_volume * 0.01
result *= (1-percentage_result)
# result * (100 - percentage_volume) / 100

print(f'{result:.3f}')
