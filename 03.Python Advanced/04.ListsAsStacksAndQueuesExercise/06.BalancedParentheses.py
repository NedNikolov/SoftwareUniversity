expression = input()

stack = []
balanced = True
for ch in expression:
    if ch in '{[(':
        stack.append(ch)
    else:
        if len(stack) == 0:
            balanced = False
            break
        last_opening_bracket = stack.pop()
        pair = f'{last_opening_bracket}{ch}'
        if pair not in '()[]{}':
            balanced = False
            break

if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")



# from collections import deque
#
# bracelets = input()
# parentheses = deque()
# problem = False
# for _ in range(len(bracelets)):
#     parentheses.append(bracelets[_])
# length = int(len(parentheses) / 2)
# for i in range(length):
#     start = parentheses[0]
#     end = parentheses[-1]
#     if start == '(':
#         if end != ')':
#             problem = True
#     elif start == '[':
#         if end != ']':
#             problem = True
#     elif start == '{':
#         if end != '}':
#             problem = True
#     if problem:
#         break
#     parentheses.pop()
#     parentheses.popleft()
# if problem:
#     print("NO")
# else:
#     print("YES")
