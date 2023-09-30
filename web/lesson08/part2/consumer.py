from time import sleep

import connect_mongodb

from connect_rabbitmq import channel
from models import Contact


channel.queue_declare(queue='queue')


def send_email(_id):
    contact = Contact.objects.get(id=_id)
    print(f'Sending email to {contact.fullname}')

    sleep(1)

    contact.is_send = True
    contact.save()


def callback(ch, method, properties, body):
    _id = body.decode('utf-8')
    send_email(_id)


channel.basic_consume(queue='queue', on_message_callback=callback, auto_ack=True)

print('[X] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
