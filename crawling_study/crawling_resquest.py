# 라이브러리 임포트
import requests # 웹페이지 가져오는 라이브러리
from bs4 import BeautifulSoup # 웹페이지 분석(크롤링) 라이브러리

# 웹페이지 가져오기
res = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=아이폰') 
soup = BeautifulSoup(res.content, 'html.parser') # res.content : 웹페이지의 정보를 가져옴
                                                 # soup에 html 파일을 파싱한 정보가 들어감
# 웹페이지 파싱하기
    # mydata = soup.find('title')
mydata = soup.select('.news_tit')

# 추출한 데이터 활용하기
for item in mydata:
    print(item.get_text().strip())