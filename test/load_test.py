import csv
import random
import molotov
import time
from os import path, environ

_URLS_FILE = path.join(path.dirname(__file__), 'urls.csv')
_API = environ.get('MOLOTOV_HOSTNAME') or 'http://localhost:8080'


# Read urls from a csv file for further use
urls = []
with open(_URLS_FILE, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        urls.append(row[0])


@molotov.scenario(weight=99)
async def test_post_get(session):
    # Grab a random url from the list
    url = random.choice(urls)

    # First off, get a shortened url id
    async with session.post(_API, json={'url': url}) as response:
        json = await response.json()
        assert response.status == 200
        assert json['_id']
        assert json['originalURL'] == url

        short_id = json['_id']

    # Then use that id to get a redirect
    async with session.get(path.join(_API, short_id), allow_redirects=False) as response:
        assert response.status == 302
        assert response.headers['Location'] == url


@molotov.scenario(weight=1)
async def test_404(session):
    # Then use that id for a redirect
    short_id = 'something-that-does-not-exist'
    async with session.get(path.join(_API, short_id), allow_redirects=False) as response:
        assert response.status == 404


# Helpers used to measure concurrency

concurs = []  # [(timestamp, worker count)]


def _now():
    return time.time() * 1000


@molotov.events()
async def record_time(event, **info):
    if event == 'current_workers':
        concurs.append((_now(), info['workers']))


@molotov.global_teardown()
def display_average():
    delta = max(ts for ts, _ in concurs) - min(ts for ts, _ in concurs)
    average = sum(value for _, value in concurs) * 1000 / delta
    print("\nAverage concurrency: %.2f VU/s" % average)
