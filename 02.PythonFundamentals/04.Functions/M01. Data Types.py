def defining_input(typ, inpt):
    if typ == 'int':
        print(f'{int(inpt) * 2}')
    elif typ == 'real':
        print(f'{float(inpt) * 1.5:.2f}')
    else:
        print(f'${inpt}$')


input_type = input()
input_input = input()
defining_input(input_type, input_input)
