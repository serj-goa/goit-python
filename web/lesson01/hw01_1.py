from abc import ABCMeta, abstractmethod
from json import dump as js_dump
from json import load as js_load
from pickle import dump as pk_dump
from pickle import load as pk_load


class SerializationInterface(metaclass=ABCMeta):
    @abstractmethod
    def load_data(self, filepath):
        pass

    @abstractmethod
    def save_data(self, filepath, data):
        pass


class BinSerializer(SerializationInterface):

    def load_data(self, filepath):
        with open(filepath, 'rb') as fh:
            return pk_load(fh)

    def save_data(self, filepath, data):
        with open(filepath, 'wb') as fh:
            pk_dump(data, fh)


class JsonSerializer(SerializationInterface):
    def load_data(self, filepath):
        with open(filepath, encoding='utf-8') as fh:
            return js_load(fh)

    def save_data(self, filepath, data):
        with open(filepath, 'w', encoding='utf-8') as fh:
            js_dump(data, fh)


bin_ser = BinSerializer()
js_ser = JsonSerializer()

some_data = {
    'world': 5,
    'python': '6',
    'ГоИТ': 'Пайтон',
    'arr': ['a', 'b', 'c']
}

js_ser.save_data(filepath='data.json', data=some_data)
bin_ser.save_data(filepath='data.bin', data=some_data)

from_js = js_ser.load_data(filepath='data.json')
from_bin = bin_ser.load_data(filepath='data.bin')

print(f'from_js: {from_js}')
print(f'from_bin: {from_bin}')
