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

#썸네일 선택 구문
images = driver.find_elements(By.CSS_SELECTOR, ".bRMDJf.islir")[0]

#이름 설정용 변수
count = 1

#반복문
for image in images:
    image.click()
    time.sleep(3)
    imgUrl = driver.find_element(By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
    count = count + 1


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()