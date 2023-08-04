# start command example
# python hw05.py -e 2

import argparse
import asyncio
import platform

from datetime import date
from pprint import pprint

import aiohttp

URL = 'https://api.privatbank.ua/p24api/exchange_rates?date='
CURRENCIES = ['USD', 'EUR']


def create_urls(count):
    today = date.today()
    urls = []

    for _ in range(count):
        dt = date(today.year, today.month, today.day - 1)
        urls.append(URL + str(dt.strftime('%d.%m.%Y')))
        today = dt

    return urls


def parse_json_resp(jsn):
    data = jsn
    date = data['date']
    curr = data['exchangeRate']
    result = {}

    for j in CURRENCIES:
        for i in curr:
            if i['currency'] == j:
                purchaseRate = (i['purchaseRate'])
                saleRate = (i['saleRate'])

        result[j] = {"purchase": purchaseRate, "sale": saleRate}

    return {date: result}


async def resp_url(url):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url) as resp:
            print(resp.status)
            json_data = await resp.json()

    return json_data


async def main():
    result = []

    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--exchange", "-e", help="exchange currency", default=1)
    args = vars(parser.parse_args())
    count_days = int(args['exchange'])

    tasks = [asyncio.create_task(resp_url(url)) for url in create_urls(count_days)]

    for task in tasks:
        resp = await task
        resp = parse_json_resp(resp)
        result.append(resp)

    return result


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    r = asyncio.run(main())
    pprint(r)
