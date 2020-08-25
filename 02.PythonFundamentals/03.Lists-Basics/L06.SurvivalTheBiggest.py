import sys

cards = input().split()
remove = int(input())
length = len(cards)
smallest = sys.maxsize

for i in range(remove):
    for j in range(length):
        if int(cards[j]) < smallest:
            smallest = int(cards[j])
    cards.remove(str(smallest))
    smallest = sys.maxsize
    length -= 1
for k in range(0, len(cards)):
    cards[k] = int(cards[k])
print(cards)
