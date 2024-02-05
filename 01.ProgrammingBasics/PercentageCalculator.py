print(f"Здравейте,")
print(f"Това е процентов калкулатор.")
print(f"Изберете валута:", end="")
currnency_input = input()

print(f"Изберете 1 за: Колко е определена стойност в процент от цялата стойност.")
print(f"Изберете 2 за: Колко процента е определена стойност от цялата стойност.")
print(f"Изберете 3 за: Колко процента са от определена стойност.")
command = int(input())

while command != 4:
    if command == 1:
        print(f"Колко е определена стойност в процент от цялата стойност.")
        print(f"Процент:", end="")
        percent = int(input())
        print(f"Обща стойност:", end="")
        total = int(input())

        result = (total * percent) / 100
        print(f"{percent}% от {total}{currnency_input}. са {result:.2f}{currnency_input}")
    elif command == 2:
        print(f"Колко процента е определена стойност от цялата стойност.")
        print(f"Търсена стойност:", end="")
        value = int(input())
        print(f"Обща стойност:", end="")
        total = int(input())

        result = 100 / (total / value)
        print(f"{value}{currnency_input} от {total}{currnency_input} са {result:.2f}%")
    else:
        print(f"Колко процента са от определена стойност.")
        print(f"Обща стойност:", end="")
        value = int(input())
        print(f"Процент:", end="")
        percentage = int(input())

        result = (percentage / 100) * value
        print(f"{percentage}% от {value}{currnency_input} са {result}{currnency_input}")
    print(f"Ако желаете да излезете изберете 4, ако желаете да калкулирате отново изберете следователно 1, 2 или 3.")
    command = int(input())
