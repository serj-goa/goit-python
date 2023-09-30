import json

import connect
import models as m


with open('authors.json') as file:
    authors_data = json.load(file)

with open('quotes.json') as file:
    quotes_data = json.load(file)

for author_data in authors_data:
    author = m.Author(**author_data)
    author.save()

for quote_data in quotes_data:
    author_name = quote_data['author']
    author = m.Author.objects(fullname=author_name).first()

    if author:
        quote_data['author'] = author
        quote = m.Quote(**quote_data)
        quote.save()
