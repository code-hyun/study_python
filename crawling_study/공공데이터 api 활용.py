import requests
from bs4 import BeautifulSoup
import openpyxl



service_key = '자신이 발급받은 서비스키'
# {'serviceKey' : '서비스키', 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'searchDate' : '2020-11-14', 'InformCode' : 'PM10' }
params = '&returnType=xml&numOfRows=100&pageNo=searchDate=2020-11-14&InformCode=PM10'

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width= 50
excel_sheet.column_dimensions['C'].width= 50
excel_sheet.append(['번호','날짜','pm 지수'])

open_api = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth?serviceKey='+ service_key + params

res = requests.get(open_api)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('item')


for index in range(100):
    
    if res.status_code == 200:
        for item in data:
            data_time = item.find('datatime')
            pm10grade = item.find('informcode')
            print(data_time.get_text(), pm10grade.get_text())
            excel_sheet.append([index+1, data_time.get_text(), pm10grade.get_text()])

    else:
        print("Error Code", res.status_code)

excel_file.save('micro_particle.xlsx')
excel_file.close()