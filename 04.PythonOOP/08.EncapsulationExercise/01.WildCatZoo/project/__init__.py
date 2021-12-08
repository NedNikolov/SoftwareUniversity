file = """worker""".split("\n")

for file in file:
    file = file + ".py"
    open(file, "a").close()