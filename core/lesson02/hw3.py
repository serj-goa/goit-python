start = True
try_item = False
operation = False

min_item = True
min_item_if = False

plus_item = True
plus_item_if = False

div_item = True
div_item_if = False

mult_item = True
mult_item_if = False

answ = 0

equals = '='
minus = '-'
plus = '+'
division = '/'
mult = '*'

oper_item = ''

while start:
    nmbr = input('Enter number: ')

    try:
        nmbr = float(nmbr)
        try_item = True

    except ValueError:
        print(f'{nmbr} is not a number')

    if try_item == True:
        answ += nmbr
        operation = True

    while operation:
        math_oper = input('Enter mathem.-operator (+, -, *, /): ')

        try:

            if math_oper == minus:

                while min_item:
                    nmbr = input('Enter number: ')

                    try:
                        nmbr = float(nmbr)
                        min_item_if = True

                        if min_item_if == True:
                            answ -= nmbr
                            min_item = False

                    except ValueError:
                        print(f'{nmbr} is not a number')

            elif math_oper == plus:

                while plus_item:
                    nmbr = input('Enter number: ')

                    try:
                        nmbr = float(nmbr)
                        plus_item_if = True

                        if plus_item_if == True:
                            answ += nmbr
                            plus_item = False

                    except ValueError:
                        print(f'{nmbr} is not a number')

            elif math_oper == division:

                while div_item:
                    nmbr = input('Enter number: ')

                    try:
                        nmbr = float(nmbr)
                        div_item_if = True

                        if div_item_if == True:
                            answ /= nmbr
                            div_item = False

                    except ValueError:
                        print(f'{nmbr} is not a number')

                    except ZeroDivisionError:
                        print(f"You entered 0, division by zero is prohibited!")

            elif math_oper == mult:

                while mult_item:
                    nmbr = input('Enter number: ')

                    try:
                        nmbr = float(nmbr)
                        mult_item_if = True

                        if mult_item_if == True:
                            answ *= nmbr
                            mult_item = False

                    except ValueError:
                        print(f'{nmbr} is not a number')

            elif math_oper == equals:
                operation = False
                start = False

        except ValueError:
            print(f'{math_oper} is not a math. operator')

print('Example solution = ' + str(answ))
