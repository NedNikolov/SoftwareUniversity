cards = input().split()
shuffle = int(input())
first_half = [' '] * len(cards)
length = len(cards)
counter = 0
for j in range(shuffle):
    for i in range(0, int(length / 2)):
        first_half[counter] = cards[i]
        first_half[counter + 1] = cards[int((len(cards) / 2) + i)]
        counter += 2
    cards = first_half.copy()
    first_half = [' '] * len(cards)
    counter = 0
print(cards)
