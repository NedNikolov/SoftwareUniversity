mountainDict = {
    "m1": {
        "mountain": "Hemus",
        "peak": "Botev",
        "summit": "2376"
    },
    "m2": {
        "mountain": "Rila",
        "peak": "Musala",
        "summit": "2925"
    },
    "m3": {
        "mountain": "Pirin",
        "peak": "Vihren",
        "summit": "2914"
    }
}

mountainDict["m4"] = {"mountain": "Rodopi", "peak": "Golqm Perelik", "summit": "2191"}

for i in mountainDict.items():
    print(i)
