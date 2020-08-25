n = int(input())
positives = []
negatives = []

for i in range(n):
    curr_num = int(input())
    if curr_num >= 0:
        positives.append(curr_num)
    else:
        negatives.append(curr_num)
print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')
