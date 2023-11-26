from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = os.path.join(current_dir, 'chromedriver.exe')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'https://unagi-hirokawa.jp/orders/kr/calendar'
driver.get(url)

# 페이지 로딩을 위해 잠시 대기
time.sleep(5)

# 현재 페이지의 소스 코드를 가져옴
# page_source = driver.page_source

# BeautifulSoup을 사용하여 HTML을 파싱
# soup = BeautifulSoup(page_source, 'html.parser')
checkbox = driver.find_element_by_id("terms")
print(checkbox)
checkbox.click()

# 동의 버튼 클릭
agree_button = driver.find_element_by_id("btn_next")
print(agree_button)
agree_button.click()


driver.quit()
