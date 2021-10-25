text = input()
words = {}

for ch in text:
    if ch in words:
        words[ch] += 1
    else:
        words[ch] = 1

print(words)
for letter, count in sorted(words.items()):
    print(f'{letter}: {count} time/s')
