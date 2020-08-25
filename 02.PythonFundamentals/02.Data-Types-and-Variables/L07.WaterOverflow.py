n = int(input())
tank_litters = 0
for i in range(0, n):
    liters = int(input())
    if 255 >= liters:
        if tank_litters + liters <= 255:
            tank_litters += liters
        else:
            print("Insufficient capacity!")
    else:
        print("Insufficient capacity!")
print(tank_litters)
