from abc import ABC, abstractmethod


class Interface(ABC):
    """Base class for the data retrieval environment."""

    @abstractmethod
    def get_msg(self):
        """"""


class InterfaceCMD(Interface):
    """Console interface for getting values from the user."""

    def get_msg(self):
        user_input = input('cmd >>> ').strip()

        return user_input


if __name__ == '__main__':
    interface = InterfaceCMD()

    print('Please, enter your command: ')
    user_input = interface.get_msg()
    print(user_input)
