n = int(input())
boolean = True
for i in range(0, n):
    symbol = input()
    if symbol == '(':
        boolean = False
    if symbol == ")" and boolean:
        boolean = False
        symbol = ''
    if not boolean and symbol == ')':
        boolean = True

if boolean:
    print('BALANCED')
else:
    print('UNBALANCED')
