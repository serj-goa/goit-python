while True:

    user_length = input('Enter a number, the length of the Fibonacci sequence: ')

    try:
        user_length = int(user_length)
        break
    
    except:
        print('Not a number\n')
        continue


def fibonacci(n):
    if 0 < n <= 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(user_length))
