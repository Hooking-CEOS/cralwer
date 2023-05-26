from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

# 환경변수 불러오기
load_dotenv()

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.instagram.com/')
# driver.get('https://www.instagram.com/freshian.official/')

driver.implicitly_wait(20)

# login_btn = driver.find_element(By.CLASS_NAME, "button[type='button']._acan _acap _acas _aj1-")
# login_btn.click()

# driver.implicitly_wait(10)

# 로그인 데이터 입력 (수정은 .env파일 사용)
# 아이디 입력
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
username_input.send_keys(os.environ.get('Instagram_ID'))

# 비밀번호 입력
userpw_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
userpw_input.send_keys(os.environ.get("Instagram_PW"))

submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_btn.click()

