import requests
from bs4 import BeautifulSoup
import json
    
class crawling_test:
    @staticmethod
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
    
    @staticmethod
    def daum():
        response = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%82%BC%EC%84%B1")
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.select(".tit_main")  # 결과는 리스트
        result = []

        for link in links:
            title = link.text
            url = link['href']
            data = {
                'title': title,
                'url': url
            }
            result.append(data)

        json_data= json.dumps(result, ensure_ascii=False)
        return json_data