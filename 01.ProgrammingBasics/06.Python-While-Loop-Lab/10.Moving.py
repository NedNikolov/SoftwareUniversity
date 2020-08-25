width = int(input())
length = int(input())
height = int(input())
cardboard = input()
result = width * length * height
apartment = 0

while cardboard != "Done" and apartment < result:
    cardboard = int(cardboard)
    apartment += cardboard

    if apartment > result or (cardboard == "Done" and apartment > result):
        cardboard = '1'
    else:
        cardboard = input()
if apartment > result:
    print(f'No more free space! You need {apartment - result} Cubic meters more.')
else:
    print(f'{result - apartment} Cubic meters left.')
