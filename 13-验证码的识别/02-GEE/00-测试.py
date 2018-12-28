import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)
browser.get('https://account.geetest.com/login')
button = browser.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
button.click()