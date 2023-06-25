# urllib + bs4 : 기존에 사용했던 라이브러리, 경우에 따라 예전 사이트의 경우 정상적으로 데이터를 가져오기 위하여 쓰임
import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=아이폰')
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select('.news_tit')
for item in data:
    print(item.get_text().strip())