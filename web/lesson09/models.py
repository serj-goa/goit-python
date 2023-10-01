from mongoengine import CASCADE, Document, ReferenceField
from mongoengine.fields import ListField, StringField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=100))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
