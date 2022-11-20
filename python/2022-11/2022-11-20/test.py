import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'https://finance.naver.com/'

response = requests.get(url)    # 해당 url에 대한 요청의 응답 저장
response.raise_for_status()     # 200 OK 코드가 아닌 경우 에러 발동
html = response.text            # text 속성을 통해 UTF-8로 인코딩된 문자열을 받을 수 있다.
soup = BeautifulSoup(html, 'html.parser') # 응답받은 HTML 내용을 BeautifulSoup 클래스의 객체 형태로 생성/반환합니다.
tbody = soup.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
trs = tbody.select('tr')
datas = []

for tr in trs:
    name = tr.select_one('th > a').get_text()
    current_price = tr.select_one('td').get_text()
    change_direction = tr['class'][0]
    change_price = tr.select_one('td > span').get_text()
    datas.append([name, current_price, change_direction, change_price])

write_wb = Workbook() # 워크북 생성시 워크 시트 자동으로 생성
write_ws = write_wb.create_sheet('결과') # 결과 시트 생성
for data in datas:
    write_ws.append(data)
write_wb.save(r'C:\Github\programmers\python\2022-11\2022-11-20/test.Cell')