from faker import Faker

import connect_mongodb

from connect_rabbitmq import channel, connection
from models import Contact


fake = Faker()

channel.queue_declare(queue='queue')

contacts = []

for i in range(10):
    contacts.append(
        {
            'fullname': fake.name(),
            'profession': fake.job(),
            'email': fake.email(),
            'is_send': False,
        }
    )

for contact_data in contacts:
    contact = Contact(**contact_data)
    contact.save()
    channel.basic_publish(
        exchange='',
        routing_key='queue',
        body=str(contact.id).encode(),
    )

print('[#] All data sent to queue')

connection.close()
