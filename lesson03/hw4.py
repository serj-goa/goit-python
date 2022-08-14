first_elem = 0
second_elem = 1
sequences_list = [0, 1]

while True:

    user_length = input('Enter the length of the Fibonacci sequence\nfrom 3 numbers or more: ')

    try:
        user_length = int(user_length)
        break
    
    except:
        print('Not a number\n')
        continue

for nmbr in range(0, user_length - 2):

    first_elem, second_elem = second_elem, (first_elem + second_elem)
    sequences_list.append(second_elem)

if user_length >= 2:

    print('Fibonacci sequence = ', sequences_list)

elif user_length < 2:

    print('Fibonacci sequence = ', sequences_list[0])



