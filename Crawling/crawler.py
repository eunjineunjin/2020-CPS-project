from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

search= input('검색하고자 하는 사진 입력: ')
url = f'https://www.google.com/search?q={quote_plus(search)}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjV9_Kx-sTpAhVXfd4KHZD9BcsQ_AUoAXoECBAQAw&biw=960&bih=960'


driver =  webdriver.Chrome() # 구글 크로링에서 필요한 코드
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

img = soup.select('.rg_i.Q4LuWd.tx8vtf') #클래스의 값 넣어주기

n=1
imgurl = []
for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

for i in imgurl: #반복문으로 자동으로 이미지 저장
     urlretrieve(i, str(n) + '.jpg')
     n +=1
driver.close()
