def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            print('Please enter a valid contact name!\n')
        except ValueError:
            print('Please enter a phone number!\n')
        except IndexError:
            print('Invalid command. Please enter the correct command and message.\n')
    return inner


@input_error
def command_add(user_data_list: list) -> None:
    if not user_data_list[1]:
        raise KeyError
    else:
        user_message = get_message(user_data_list)

        if len(user_message.split()) < 2:
            raise ValueError

        contact_name = get_contact_name(user_message)
        phone = get_contact_phone(user_message)

        if contact_name in phonebook:
            raise KeyError
        elif not phone:
            raise ValueError
        else:
            phonebook[contact_name] = phone


@input_error
def command_change(user_data_list: list) -> None:
    if not user_data_list[1]:
        raise KeyError
    else:
        user_message = get_message(user_data_list)

        if len(user_message.split()) < 2:
            raise ValueError

        contact_name = get_contact_name(user_message)
        phone = get_contact_phone(user_message)

        if not contact_name in phonebook:
            raise KeyError
        elif not phone:
            raise ValueError
        else:
            phonebook[contact_name] = phone


def command_close_program(_) -> None:
    print('Good bye!\n')
    quit()


def command_hello(_) -> None:
    print('How can I help you?\n')


def command_help(_) -> None:
    print('''
"hello"                      - greetings.
"add <new_name> <new_phone>" - adding a new contact.
"change <name> <new_phone>"  - change the phone number of an existing contact.            
"phone <name>"               - show phone numbers for an existing contact.
"show all"                   - show all saved contacts with phone numbers.
"good bye", "close", "exit"  - exit from the program. 
    ''')


@input_error
def command_phone(user_data_list: list) -> None:
    if not user_data_list[1]:
        raise KeyError
    else:
        user_message = get_message(user_data_list)
        contact_name = get_contact_name(user_message)
        if contact_name in phonebook:
            print(f'{contact_name}: {phonebook[contact_name]}\n')
        else:
            raise KeyError


def command_show_all(_) -> None:
    print()
    for name, phone in phonebook.items():
        print(f'{name}: {phone}')
    print()


@input_error
def get_command(some_data: list) -> str:
    if not some_data[0]:
        raise IndexError
    else:
        user_command = some_data[0].lower()
    return user_command


@input_error
def get_message(some_data: list) -> str:
    if not some_data[1]:
        raise IndexError
    else:
        user_message = some_data[1].strip()
    return user_message


@input_error
def get_contact_name(some_string: str) -> str:
    data_lst = some_string.rsplit(' ', 1)
    if len(data_lst) >= 1:
        if not data_lst[-1].isalpha():
            contact_name = data_lst[0]
        else:
            contact_name = some_string
        return contact_name
    else:
        raise IndexError


def get_contact_phone(some_string: str) -> str:
    data_lst = some_string.rsplit(' ', 1)
    if len(data_lst) > 1:
        phone = data_lst[1]
    return phone


def parse_command_and_message(user_input: str) -> list:
    separator = ' '
    for cmd in PROGRAM_CMD:
        if user_input.lower().startswith(cmd):
            separator = cmd
            user_input = cmd + user_input[len(cmd) + 1:]
            break

    some_string_lst = user_input.split(separator, 1)
    if separator != ' ':
        some_string_lst[0] = separator
    return some_string_lst


@input_error
def run_command(user_data_list: list) -> None:
    if not user_data_list[0]:
        raise IndexError
    else:
        user_command = get_command(user_data_list)

        if PROGRAM_CMD.get(user_command) is None:
            raise IndexError
        else:
            PROGRAM_CMD[user_command](user_data_list)


def main():
    print('Please, enter your command: ')

    while True:
        user_input = input('cmd >>> ').strip()
        user_data_list = parse_command_and_message(user_input)
        run_command(user_data_list)


if __name__ == '__main__':

    phonebook = {'Alex': '5674532', 'Ivan': '23464878'}
    PROGRAM_CMD = {
        'add': command_add, 
        'change': command_change, 
        'phone': command_phone,
        'hello': command_hello,
        'help': command_help,
        'show all': command_show_all,
        'good bye': command_close_program,
        'close': command_close_program, 
        'exit': command_close_program
        }

    main()
