import requests
from bs4 import BeautifulSoup
import json


def naver():
    response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=삼성")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")  # 결과는 리스트
    result = []

    for link in links:
        title = link.text
        url = link['href']
        data = {
            'title': title,
            'url': url
        }
        result.append(data)

    json_data = json.dumps(result, ensure_ascii=False)
    return json_data
