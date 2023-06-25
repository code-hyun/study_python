import requests # 해당 데이터를 제공해주는 컴퓨터, 주소를 통해 특정 데이터를 갖는 api
import openpyxl

client_id = '발급 받은 키' # 네이버 키
client_secret = '발급 받은 키' # 

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 100
excel_sheet.append(['랭킹','제목','링크'])

start, num = 1, 0
for index in range(10):
    start_num = start + (index * 100)    
    naver_open_api =  'https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=' + str(start_num)
    header_params = {"X-Naver-Client-id" : client_id , "X-Naver-Client-Secret":client_secret}
               # get 방식
    res = requests.get(naver_open_api, headers=header_params) # request.get(url), request.get(url,추가할 정보(헤더값을 추가))
    #data = res.json()
    #print(data)

    # json 데이터를 불러올 때 오류가 발생 할 수 있기 때문에 if문으로 error 코드를 만들어준다.(일반적으로 써줌)
    if res.status_code == 200:
        data = res.json()

    #     print(res.text) 보기 편하게 나온다
    #     pprint.pprint(data['items'][0]['title'])
    #     pprint.pprint(data)
        for item in data['items']: # enumerate : index 번호를 쓸 수 있다.
            num += 1
            excel_sheet.append([num, item['title'], item['link']])
    else:
        print("Error Code", res.status_code)

excel_file.save('IT.xlsx')
excel_file.close()