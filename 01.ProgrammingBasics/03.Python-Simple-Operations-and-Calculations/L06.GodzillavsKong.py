movie_budget = float(input())
helper_count = int(input())
clothes_prise = float(input())

decor = movie_budget * 0.10
clothes_prise *= helper_count
if helper_count > 150:
    clothes_prise *= 0.90

prise = decor + clothes_prise

if movie_budget < prise:
    print("Not enough money!")
    print(f"Wingard needs {abs(movie_budget - prise):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(movie_budget - prise):.2f} leva left.")
