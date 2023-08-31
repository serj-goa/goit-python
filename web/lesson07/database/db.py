import pathlib
import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


config_path = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(config_path)

username = config.get('DB', 'user')
password = config.get('DB', 'password')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')
port = config.get('DB', 'port')

url = f'postgresql://{username}:{password}@{domain}:{port}/{db_name}'

engine = create_engine(url, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()
