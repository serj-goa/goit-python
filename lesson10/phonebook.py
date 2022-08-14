from collections import UserDict
from typing import List


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self) -> str:
        result = ''

        for name, record in self.data.items():
            phones = []

            for all_phones in record.phone:
                phones.append(all_phones.value)

            result += f'{name}: {", ".join(phones)}\n'

        return result



class Field:
    """Class Field is parent for all fields in Record class"""
    def __init__(self, value: str) -> None:
        self.value = value


class Name(Field):
    """Class Name for storage name's field"""


class Phone(Field):
    """Class Phone for storage phone's field"""


class Record:
    """Record class responsible for the logic of adding/removing/editing fields"""
    def __init__(self, name: Name, phone: List[Phone] = None) -> None:
        self.name = name
        self.phone = [] if phone is None else [phone]

    def add_new_phone(self, new_phone: Phone) -> None:
        self.phone.append(new_phone)

    def change_phone(self, phone_indx: int, new_phone: Phone) -> None:
        self.phone[phone_indx] = new_phone

    def delete_phone(self, remove_phone: Phone) -> None:
        self.phone.remove(remove_phone)


if __name__ == '__main__':
    book = AddressBook()

    serj = Name('Serj')
    serj_phone = Phone('321432546')
    rec_serj = Record(serj, serj_phone)

    new_phone_1 = Phone('433465675')
    new_phone_2 = Phone('753367888')

    rec_serj.add_new_phone(new_phone_1)
    rec_serj.add_new_phone(new_phone_2)

    print('rec_name: ', rec_serj.name.value)
    print('rec_phone: ', rec_serj.phone)

    rec_serj.change_phone(phone_indx=0, new_phone=Phone('11111111111'))
    rec_serj.delete_phone(new_phone_2)


    print('\nrec_phone after deleting phone: ', rec_serj.phone)
    print('rec_phone after change: ', rec_serj.phone[0].value)

    book.add_record(record=rec_serj)
    print('\nbook: ', book.data)
    print(f'book values: {book.data["Serj"]}')
