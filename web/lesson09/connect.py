import configparser

from mongoengine import connect


config = configparser.ConfigParser()
config.read('config.ini')

mongodb_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

connect(
    host=f'''mongodb+srv://{mongodb_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority''',
    ssl=True,
)
