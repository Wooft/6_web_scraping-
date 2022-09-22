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

base_url = 'https://habr.com'
end_url = '/ru/all/'

def getsoup(link):
    response = requests.get(link, headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    return soup

def getlinks():
    links = []
    urls = []
    urls.append(base_url + end_url)
    for i in range(2, 6):
        urls.append(base_url + end_url + f'page{i}')
    for url in urls:
        soup = getsoup(url)
        articles = soup.find_all("article")
        for article in articles:
            if 'company' not in article.find(class_="tm-article-snippet__title-link").attrs["href"]:  ##удаляем рекламные посты
                links.append(base_url + article.find(class_="tm-article-snippet__title-link").attrs["href"])
    print(f'Всего найдено статей за последние 5 дней: {len(links)}.')
    return links

def getstats():
    links = getlinks()
    number = 0
    for link in links:
        flag = 0
        soup = getsoup(link)
        text = soup.find(class_="article-formatted-body").text
        for words in KEYWORDS:
            if words in text.strip():
                if flag == 0:
                    number += 1
                    print(f'{number}. Статья: "{soup.find(class_="tm-article-snippet__title tm-article-snippet__title_h1").text}", ссылка - {link} содержит ключевое слово - "{words}"')
                    flag = 1
                else:
                    print(f'А также, ключевое слово: "{words}"')

if __name__ == '__main__':
    getstats()