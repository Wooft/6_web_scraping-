import pprint
import bs4
import requests

headers = {
    'sec-ch-ua': 'Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document'
}
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = 'https://habr.com/ru/all/'

def getinfo():
    response = requests.get(url=base_url, headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all("article")
    for article in articles:
        hubs = article.find_all(class_="tm-article-snippet__hubs-item")
        hubs = [hub.text.strip() for hub in hubs ]
        print(hubs)

if __name__ == '__main__':
    getinfo()