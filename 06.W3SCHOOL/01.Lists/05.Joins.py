males = ["Ivan", "Stoyan", "Georgi", "Dimitar"]
fmales = ["Ivanka", "Stoika", "Gergana", "Dimitriya"]

namesFirst = males + fmales
print(namesFirst)

for x in fmales:
    males.append(x)
print(males)

males.append(fmales)
print(males)

