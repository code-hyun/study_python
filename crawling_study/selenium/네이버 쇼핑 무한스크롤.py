from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# # 웹페이지 해당 주소 이동
driver.get("http://www.naver.com")
# driver.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌

# 쇼핑메뉴 클릭
print(driver.find_element('#shortcutArea > ul > li:nth-child(4) > a > span.service_name'))
driver.find_element('.event_bg_wrap').click()
# time.sleep(5)
 
# 검색창 클릭
search = driver.find_element('input.co_srh_input._input')
search.click()

# 검색어 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = driver.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    driver.find_element("body").send_keys(Keys.END)
    
    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)
    
    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")
    
    if after_h == before_h :
        break
    after_h == before_h
