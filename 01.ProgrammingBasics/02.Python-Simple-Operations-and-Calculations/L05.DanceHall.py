import math

length = float(input())
width = float(input())
side = float(input())

hall_size = (length * 100) * (width * 100)
wardrobe_size = (side * 100) * (side * 100)
bench_size = hall_size / 10
free_space_dancer = hall_size - (wardrobe_size + bench_size)
free_space_dancer /= 7040

print(math.floor(free_space_dancer))
