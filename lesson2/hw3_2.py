calc_result = 0
user_operator = None

while user_operator != '=':
    try:
        user_nmbr = input('Please enter your number: ')
        user_nmbr = float(user_nmbr)    
        
    except ValueError:
        print('Enter a number!')
        continue

    if user_operator == None:
        calc_result = user_nmbr

    elif user_operator == '+':
        calc_result += user_nmbr

    elif user_operator == '-':
        calc_result -= user_nmbr

    elif user_operator == '*':
        calc_result *= user_nmbr

    elif user_operator == '/':
        
        try:
            calc_result /= user_nmbr
            
        except ZeroDivisionError:
            print("Zero division error!")
            continue

    user_operator = input('Please enter operator "+, -, *, /" or " = " for quit: ')

    while user_operator not in ('+', '-', '*', '/', '='):

        print("Enter only operator symbol '+', '-', '*', '/', '='")
        user_operator = input('Please enter operator: ')

    if user_operator == '=':
        continue

print(f'  Your result is {calc_result}')
