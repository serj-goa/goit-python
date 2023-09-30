from mongoengine import Document
from mongoengine.fields import BooleanField, StringField


class Contact(Document):
    fullname = StringField()
    profession = StringField()
    email = StringField()
    is_send = BooleanField(default=False)
