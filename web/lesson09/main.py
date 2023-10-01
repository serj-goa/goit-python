import json

import bs4
import requests


def get_quotes():
    url = 'http://quotes.toscrape.com'
    quotes = []

    while True:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'lxml')

        for quote_div in soup.find_all('div', class_='quote'):
            quote = {
                'tags': [
                    tag.get_text() for tag in quote_div.find_all('a', class_='tag')
                ],
                'author': quote_div.find('small', class_='author').get_text(),
                'quote': quote_div.find('span', class_='text').get_text(),
            }
            quotes.append(quote)

        next_page = soup.find('li', class_='next')

        if next_page:
            url = url + next_page.find('a')['href']

        else:
            break

    return quotes


def save_quotes(quotes):
    with open('quotes.json', 'w', encoding='utf-8') as file:
        json.dump(quotes, file, ensure_ascii=False)


def get_authors():
    url = 'http://quotes.toscrape.com'
    authors = []

    while True:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'lxml')

        for author_div in soup.find_all('div', class_='quote'):
            author = {
                'fullname': author_div.find('small', class_='author').get_text()
            }
            about = url + author_div.find('small', class_='author').find_next('a')['href']
            inner_resp = requests.get(about)
            inner_soup = bs4.BeautifulSoup(inner_resp.content, 'html.parser')
            data_born = inner_soup.select('span.author-born-date')
            data_born_text = ''.join([d.text.strip() for d in data_born])

            location_born = inner_soup.select('span.author-born-location')
            location_born_text = ''.join([l.text.strip() for l in location_born])

            desc = inner_soup.select('div.author-description')
            desc_text = ''.join([d.text.strip() for d in desc])

            author.update(
                {
                    'born_date': data_born_text,
                    'born_location': location_born_text,
                    'description': desc_text,
                }
            )

            if author['fullname'] not in [a['fullname'] for a in authors]:
                authors.append(author)

        next_page = soup.find('li', class_='next')

        if next_page:
            url = url + next_page.find('a')['href']

        else:
            break

    return authors


def save_authors(authors):
    with open('authors.json', 'w', encoding='utf-8') as file:
        json.dump(authors, file, ensure_ascii=False)


if __name__ == '__main__':
    quotes = get_quotes()
    save_quotes(quotes)

    authors = get_authors()
    save_authors(authors)
