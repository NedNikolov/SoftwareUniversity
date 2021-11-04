print(f"Здравейте,")
print(f"Това е процентов калкулатор.")
print(f"Изберете 1 за: Колко е определена стойност в процент от цялата стойност")
print(f"Изберете 2 за: Колко процента е определена стойност от цялата стойност")
print(f"Изберете 3 за: Колко са 100% от определена стойност")
command = int(input())

while command != 4:
    if command == 1:
        print(f"Колко е определена стойност в процент от цялата стойност")
        print(f"Percentage:", end="")
        percent = int(input())
        print(f"Total:", end="")
        total = int(input())

        result = (total * percent) / 100
        print(f"{percent}% от {total} са {result:.2f}")
    elif command == 2:
        print(f"Колко процента е определена стойност от цялата стойност")
        print(f"Value:", end="")
        value = int(input())
        print(f"Total:", end="")
        total = int(input())

        result = 100 / (total / value)
        print(f"{value}% от {total} са {result:.2f}%")
    else:
        print(f"Колко са 100% от определена стойност")
        print(f"Value:", end="")
        value = int(input())
        print(f"Percentage:", end="")
        percentage = int(input())

        result = (100 / percentage) * value
        print(f"100% от {value} са {result}")
    print(f"Ако желаете да излезете изберете 4, ако желаете да калкулирате отново изберете следователно 1, 2 или 3")
    command = int(input())
