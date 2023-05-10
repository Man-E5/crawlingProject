from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request



#옵션 설정(연구 필)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
chr_options.add_experimental_option("excludeSwitches", ["enable-logging"])

#드라이버 설정
driver = webdriver.Chrome(options=chr_options)

#웹페이지 열기
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")


#검색창 확인 후 검색
elem = driver.find_element(By.NAME, "q")
elem.send_keys("와우맨")
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

time.sleep(3)

#썸네일 선택 구문
images = driver.find_elements(By.CSS_SELECTOR, ".bRMDJf.islir")




#이름 설정용 변수
count = 1



#이미지 다운로드 반복문
for image in images:

    print(image)
    image.click()
    time.sleep(1)
    imgUrl = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]").get_attribute("src")

    # print(imgUrl)
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
    count = count + 1

    if count > 10:
        break


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()