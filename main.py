print('\nCalculator')
ms = 0
while True:
    print('\nStored Memory (MS) = ', ms)
    print('\nWhat would you like to do?')
    operator = input('\n1-Add / 2-Subtract / 3-Multiply / 4-Divide / 0-Exit: ')
    if operator == "0":
        break
    value_1 = float(input('\nEnter the first number: '))
    value_2 = float(input('\nEnter the second number: '))
    if operator == "1":
        result = value_1 + value_2
        print('\nResult = ', result)
    elif operator == "2":
        result = value_1 - value_2
        print('\nResult = ', result)
    elif operator == "3":
        result = value_1 * value_2
        print('\nResult = ', result)
    elif operator == "4":
        result = value_1 / value_2
        print('\nResult = ', result)
    else:
        operator = None
        print('\nInvalid operation.')
        input('\nPress any key to exit.')
        break
    print('\nDo you want to store the result (MS)?')
    memory = input('\n1-Add (M+) / 2-Subtract (M-) / "Enter"-Do Not Store / 0-Exit: ')
    if memory == '1':
        ms += result
    elif memory == '2':
        ms -= result
    elif memory == '':
        continue
    elif memory == '0':
        break
    else:
        nome = None
        print('\nInvalid input, the value was not saved.')
        continue
