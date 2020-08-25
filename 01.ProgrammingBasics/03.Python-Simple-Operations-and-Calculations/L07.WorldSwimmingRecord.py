import math

record_seconds = float(input())
distance_metres = float(input())
time_seconds = float(input())

result = distance_metres * time_seconds
added_time = (math.floor(distance_metres / 15)) * 12.5
result += added_time

if result < record_seconds:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(result - record_seconds):.2f} seconds slower.')

