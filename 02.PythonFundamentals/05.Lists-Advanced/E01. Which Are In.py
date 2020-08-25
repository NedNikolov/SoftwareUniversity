first_list = input().split(", ")
second_list = input().split(", ")
# res = [first for first in first_list for second in second_list if first in second]
restwo = []
for i in range(len(first_list)):
    for j in range(len(second_list)):
        if first_list[i] in second_list[j]:
            restwo.append(first_list[i])
# print(sorted(set(res), key=res.index))
print(sorted(set(restwo), key=restwo.index))
