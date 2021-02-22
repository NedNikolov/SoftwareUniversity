

#for ii:=0 to nBrVn-1  do begin
#Test2:=Test2+ (nGive/nBrVn)   /(power(1+GPR2, ii*nVnPer/12));

result = 0
for i in range(0, 35):
    result += ((26638.65 - 2556.46)/36) / (pow((1 + 11.48), (i * 1 / 12)))
    print(f'{result:.2f}')


print('--')
print(pow((1 + 11.48), (0 * 1 / 12)))
print('--')
print(pow((1 + 11.48), (1 * 1 / 12)))
print('--')
print('--')
print(12.48 ** (1 / 12))
final = (((26638.65 - 2556.46)/36) + 2556.46) / (pow((1 + 11.48), (36 * 1 / 12)))
print(final)
print(f'{result + final:.2f}')
