from phonebook import AddressBook, Name, Phone, Record


def input_error(func):
    """
    Generic Exception Handler.
    """
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
def command_add(user_data_list: list) -> str:
    """
    Adding a new contact to the phone book.
    """
    if not user_data_list[1]:
        raise KeyError
    else:
        user_message = get_message(user_data_list)

        if len(user_message.split()) < 2:
            raise ValueError

        contact_name = get_contact_name(user_message)
        phone = Phone(get_contact_phone(user_message))

        if not phone.value:
            raise ValueError

        if contact_name in phonebook:
            exist_record = phonebook[contact_name]
            exist_record.add_new_phone(phone)
            return contact_name
        
        else:
            new_contact_name = Name(contact_name)
            new_record = Record(new_contact_name, phone)
            phonebook[new_record.name.value] = new_record
            return contact_name


@input_error
def command_change(user_data_list: list) -> str:
    """
    Change an existing contact in the phone book.
    """
    if not user_data_list[1]:
        raise KeyError
    else:
        user_message = get_message(user_data_list)

        if len(user_message.split()) < 2:
            raise ValueError

        contact_name = get_contact_name(user_message)
        phone_data = get_contact_phone(user_message).split()
        contact_phone = phone_data[0]
        new_contact_phone = phone_data[1]

        if not contact_name in phonebook:
            raise KeyError

        elif not contact_phone:
            raise ValueError

        else:
            new_phone = Phone(new_contact_phone)
            record  = phonebook[contact_name]

            for idx, rec_phone in enumerate(record.phone):
                if rec_phone.value == contact_phone:
                    record.change_phone(phone_indx=idx, new_phone=new_phone)

            return contact_name


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
    """
    Search for an existing contact in the phone book.
    """
    if not user_data_list[1]:
        raise KeyError
    else:
        user_message = get_message(user_data_list)
        contact_name = get_contact_name(user_message)

        if contact_name in phonebook:
            record = phonebook[contact_name]
            contact_phones = [phone.value for phone in record.phone]
            print(f'{contact_name}: {", ".join(contact_phones)}\n')
        else:
            raise KeyError


def command_show_all(_) -> None:
    """
    Display all existing contacts in the phone book.
    """
    print()
    print(phonebook)


def confirmation_report(contact_name: str, user_command: tuple) -> None:
    """
    Report on the successful addition or change of contact details.
    """
    print(f'Contact {contact_name} {user_command} successful.\n')


@input_error
def get_command(some_data: list) -> str:
    """
    Getting a user command.
    """
    if not some_data[0]:
        raise IndexError
    else:
        user_command = some_data[0].lower()
    return user_command


@input_error
def get_message(some_data: list) -> str:
    """
    Receiving data (name, phone) transferred by the user.
    """
    if not some_data[1]:
        raise IndexError
    else:
        user_message = some_data[1].strip()
    return user_message


@input_error
def get_contact_name(some_string: str) -> str:
    """
    Getting the name from the data passed by the user.
    """
    data_lst = some_string.split()

    if len(data_lst) >= 1:
        name_data = []

        for data in data_lst:
            clear_data = normalize_msg(data)
            if clear_data.isdigit():
                break
            name_data.append(data)

        contact_name = ' '.join(name_data)

        return contact_name

    else:
        raise IndexError


def get_contact_phone(some_string: str) -> str:
    """
    Getting the phone from the data transmitted by the user.
    """
    data_lst = some_string.split()

    if len(data_lst) > 1:
        phone_data = []

        for data in data_lst[::-1]:
            clear_data = normalize_msg(data)
            if clear_data.isdigit():
                phone_data.insert(0, data)
            else:
                break

        phone = ' '.join(phone_data)

    return phone


def normalize_msg(message):
    symbols = '-+=_'
    for symb in symbols:
        message = message.replace(symb, '')
    return message


def parse_command_and_message(user_input: str) -> list:
    """
    Receiving command and data (name, phone) sent by the user.
    """
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
    """
    Run a command received from the user.
    """
    if not user_data_list[0]:
        raise IndexError
    else:
        user_command = get_command(user_data_list)

        if PROGRAM_CMD.get(user_command) is None:
            raise IndexError
        else:
            return_contact_name = PROGRAM_CMD[user_command](user_data_list)
            return user_command, return_contact_name


def main():
    print('Please, enter your command: ')

    while True:
        user_input = input('cmd >>> ').strip()
        user_data_list = parse_command_and_message(user_input)
        data_after_run_cmd = run_command(user_data_list)
        if data_after_run_cmd and data_after_run_cmd[1] is not None:
            confirmation_report(user_command=data_after_run_cmd[0], contact_name=data_after_run_cmd[1])


if __name__ == '__main__':

    phonebook = AddressBook()
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
