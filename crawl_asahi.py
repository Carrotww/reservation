from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import aws_sms

def find_available_dates(url, year, month, days):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 헤드리스 모드 활성화
    chrome_options.add_argument("--no-sandbox")  # 샌드박스 비활성화
    chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm 파티션 사용 제한 해제

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    time.sleep(5)

    # 현재 페이지의 소스 코드를 가져옴
    page_source = driver.page_source

    # BeautifulSoup을 사용하여 HTML을 파싱
    soup = BeautifulSoup(page_source, 'html.parser')

    # 예약 가능한 날짜 찾기
    available_dates = soup.find_all('a', class_='pop')

    # 특정 날짜의 예약 가능 여부 확인
    available = []
    for date in available_dates:
        href = date['href']
        for day in days:
            date_str = f'{year}-{month:02d}-{day:02d}'
            if f'date={date_str}' in href:
                available.append(date_str)

    driver.quit()
    return available

# 함수 사용 예시: 2023년 12월 2일, 3일 중 예약 가능한 날짜 찾기
url = 'https://factory.asahibeer.co.jp/reservation/?area=suita'
available_days = find_available_dates(url, 2023, 12, [2, 3, 9])

# 예약 가능한 날짜가 있으면 SMS 보내기
for available_day in available_days:
    aws_sms.main("오사카 아사히 맥주공장", available_day, url)