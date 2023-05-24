from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os



#옵션 설정(연구 필)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
chr_options.add_experimental_option("excludeSwitches", ["enable-logging"])

#드라이버 설정
driver = webdriver.Chrome(options=chr_options)


#검색 변수 설정

celebName = "박보영"
maxCap = 100

thumeClass = ".rg_i.Q4LuWd"
xPath = "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]"



#저장 환경 설정
#지정 이미지 저장 폴더 이름
outpath = "C:/Users/lenovo/Desktop/crawlingProject/crawlingProject/downImg/" + celebName + "/" 
#폴더가 존재하지 않는다면 폴더 생성
if not os.path.isdir(outpath):
    os.makedirs(outpath)



#웹페이지 열기
driver.get("https://www.google.co.kr/imghp")



#검색창 확인 후 검색
elem = driver.find_element(By.NAME, "q")
elem.send_keys(celebName)
elem.send_keys(Keys.RETURN)



#스크롤 내리기 반복문_이거 풀면 오류남 왜지
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        

        try:
            driver.find_element(By.CSS_SELECTOR, ".r0zKGf").send_keys(Keys.ENTER)
        except:
            print("d1")
    
        try:
            driver.find_element(By.CSS_SELECTOR, ".mye4qd").send_keys(Keys.ENTER)
        except:
            print("d2")
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

    last_height = new_height

time.sleep(5)

#썸네일 선택 구문
images = driver.find_elements(By.CSS_SELECTOR, thumeClass)

print(len(images))

#이름 설정용 변수
count = 1
fileName = ""



#이미지 다운로드 반복문
for image in images:

    # print(image)
    time.sleep(1)

    #오류시 넘어가부려
    try:
        image.click()
    except:
        count = count -1
        continue
    
    
    imgUrl = driver.find_element(By.XPATH, xPath).get_attribute("src")


    if count < 10:
        fileName = celebName + "_0" + str(count)
    else:
        fileName = celebName + "_" + str(count)

    
    # print(imgUrl)


    #403 회피기동 방법 1

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]

    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imgUrl, outpath+ fileName + ".jpg")

    count = count + 1

    if count > maxCap:
        break


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

#아따메 끄기
driver.close()