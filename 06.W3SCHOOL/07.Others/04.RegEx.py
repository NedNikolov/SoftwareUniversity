import re

text = "Are you there"

x = re.search("^Are.*there$", text)

print(bool(x))






