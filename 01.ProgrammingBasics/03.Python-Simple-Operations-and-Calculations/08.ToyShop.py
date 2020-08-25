travel_prize = float(input())
puzzles = float(input())
dolls = float(input())
bears = float(input())
minions = float(input())
trucks = float(input())

toys_count = puzzles + dolls + bears + minions + trucks
toys_prize = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2

if toys_count >= 50:
    toys_prize -= (toys_prize * 0.25)
    # toys_prize = toys_prize * 0.75

toys_prize -= (toys_prize * 0.10)
# toys_prize = toys_prize * 0.90

if toys_prize >= travel_prize:
    print(f"Yes! {abs(toys_prize - travel_prize):.2f} lv left.")
else:
    print(f"Not enough money! {abs(toys_prize - travel_prize):.2f} lv needed.")
