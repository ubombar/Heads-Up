

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    try:
        with closing(get(url, stream = True)) as resp:
            if is_good_response(resp):
                return resp._content
            else:
                return None
    except RequestException as e:
        print('Something caused problems: ', e)

def is_good_response(resp):
    ctype = resp.headers['Content-Type'].lower()
    return resp.status_code == 200 and ctype is not None and ctype.find('html') > -1


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Siege_of_Zara'

    print('get stuff from wikipedia')
    print(simple_get(url))


