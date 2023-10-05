from django.db import models as m


class Author(m.Model):
    fullname = m.CharField(max_length=50)
    born_date = m.CharField(max_length=50)
    born_location = m.CharField(max_length=150)
    description = m.TextField()
    created_at = m.DateTimeField(auto_now_add=True)


class Tag(m.Model):
    name = m.CharField(max_length=50, null=False, unique=True)


class Quote(m.Model):
    quote = m.TextField()
    tags = m.ManyToManyField(Tag)
    author = m.ForeignKey(Author, on_delete=m.CASCADE, null=True)
    created_at = m.DateTimeField(auto_now_add=True)
