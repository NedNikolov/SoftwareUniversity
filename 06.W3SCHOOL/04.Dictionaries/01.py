mountainDict = {"mountain": "Hemuss", "peak": "Botevv", "summit": "2376"}
print(len(mountainDict))
print(mountainDict)

mountainDict["country"] = "Bulgaria"
mountainDict.update({"cabin": "Ray"})
print(mountainDict)

highestPeak = mountainDict["peak"]
print(highestPeak)
peakHigh = mountainDict.get("summit")
print(peakHigh)

allKeys = mountainDict.keys()
allValues = mountainDict.values()
allItems = mountainDict.items()
print(allKeys)
print(allValues)
print(allItems)

mountainDict["mountain"] = "Hemus"
mountainDict.update({"peak": "Botev"})
mountainDict.pop("cabin")
mountainDict.popitem()
print(mountainDict)
mountainDict.clear()

