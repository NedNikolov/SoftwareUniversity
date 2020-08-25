import math
cards = input().split(', ')
beggars = int(input())
beggars_count = [0] * beggars
length = len(cards)

for i in range(math.ceil(length / beggars)):
    for j in range(beggars):
        if len(cards):
            beggars_count[j] = beggars_count[j] + int(cards[0])
            cards.pop(0)
print(beggars_count)
