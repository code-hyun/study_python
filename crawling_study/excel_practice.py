import requests
from bs4 import BeautifulSoup

import openpyxl

def write_excel_template(filename, sheetname, listdata):
    file = openpyxl.Workbook()
    sheet = file.active
    sheet.column_dimensions['A'].width= 100
    sheet.column_dimensions['B'].width = 20
    
    if sheetname != '':
        sheet.title = sheetname
    for item in listdata:
        sheet.append(item)
    file.save(filename)
    file.close()
    
lists = list()
page_num = 0
for num in range(10):
    if num == 0:
        res = requests.get('https://eomisae.co.kr/rt')
    else:
        res = requests.get('https://eomisae.co.kr/index.php?mid=rt&page=' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')
    
    data = soup.select('.card_el')
    for item in data:
        name = item.select_one('.card_content h3 a.pjax')
#         date = item.select('p:nth-child(1)')
        date = item.select('p span')
        date_info = date[0].get_text()+ date[1].get_text()
        info = [name.get_text().strip(), date_info]
        print(info)
        lists.append(info)
        
write_excel_template('eomisae.xlsx', '상품정보', lists)