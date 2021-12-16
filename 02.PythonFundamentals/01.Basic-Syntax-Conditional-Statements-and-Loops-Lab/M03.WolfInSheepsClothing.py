array = input().split(", ")

if array.pop() == "wolf":
    print("Please go away and stop eating my sheep")
else:
    array.reverse()

    for i in range(len(array)):
        if array[i] != "sheep":
            print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")
