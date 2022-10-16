from phonebook import AddressBook
from Notes import Notes
from pathlib import Path
from pickle import load, dump


def dump_base(file_path: Path, db: dict) -> str:

    try:
        with open(file_path, 'wb') as fh:
            dump(db, fh)

    except Exception as error:
        return error

    return 'Phonebook saved.'


def load_base(file_path: Path, dict=AddressBook()) -> AddressBook:

    try:
        with open(file_path, 'rb') as fh:
            phonebook = load(fh)

    except FileNotFoundError:
        return dict

    except EOFError:
        return dict

    return phonebook
