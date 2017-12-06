from bs4 import BeautifulSoup
import urllib3
import requests

http = urllib3.PoolManager()
def htmlgetter(url):
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html5lib")
    return soup

soup = htmlgetter('http://www.cnn.com/')
# headline = soup.find('h2', attrs={'class': "banner-text banner-text--natural"})
# headline = headline.text.strip()
soup.div.a

print(soup)
