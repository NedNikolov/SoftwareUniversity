def validation(text):
    number = 0
    letter = 0
    boolean = True
    for i in range(len(text)):
        if text[i].isdigit():
            number += 1
        elif text[i].isalpha():
            letter += 1
        else:
            print('Password must consist only of letters and digits')
            boolean = False
            break
    if (letter + number) < 6 or (letter + number) > 10:
        if boolean:
            print('Password must be between 6 and 10 characters')
            boolean = False
    if number < 2:
        print('Password must have at least 2 digits')
        boolean = False
    if boolean:
        print('Password is valid')


password = input()
validation(password)
