sentence = input().lower()
sand = 'sand'
water = 'water'
fish = 'fish'
sun = 'sun'
count = sentence.count(sand)
count += sentence.count(water)
count += sentence.count(fish)
count += sentence.count(sun)
print(count)
