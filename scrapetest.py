# using the builtin library
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

url = "http://pythonscraping.com/pages/page1.html"
try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found, check url: {}'.format(url))
else:
    print('Loaded data from: {}'.format(url))

    line = '-' * 10
    print('{}now using BeautifulSoup{}'.format(line, line))

    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html5lib")
    print(bsObj.h1)
