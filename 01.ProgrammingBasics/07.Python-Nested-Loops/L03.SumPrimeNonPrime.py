import math
command = input()
primeSum = 0
nonPrimeSum = 0
while command != 'stop':
    num = int(command)
    boolean = True
    if num == 0 or num == 1:
        boolean = False
    if num < 0:
        print("Number is negative.")
    else:
        for i in range(2, num):
            if num % i == 0 and i != num:
                boolean = False
                break
        if boolean:
            primeSum += num
        else:
            nonPrimeSum += num
    command = input()
print(f'Sum of all prime numbers is: {primeSum}')
print(f'Sum of all non prime numbers is: {nonPrimeSum}')
