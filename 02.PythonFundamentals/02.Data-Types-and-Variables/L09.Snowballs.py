n = int(input())
snow = 0
time = 0
quality = 0
result = 0
snow2 = 0
time2 = 0
quality2 = 0
current_result = 0
for i in range(0, n):
    snow = int(input())
    time = int(input())
    quality = int(input())
    current_result = int((snow / time)) ** quality
    if current_result > result:
        result = current_result
        snow2 = snow
        time2 = time
        quality2 = quality
print(f'{snow2} : {time2} = {result} ({quality2})')
