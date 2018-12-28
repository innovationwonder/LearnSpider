from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
url = 'https://www.baidu.com'
# 改写 wait 由于后面多次用到，过长
wait = WebDriverWait(browser, 10)

def search(url):
    browser.get(url) # 打开网页
    # 判断是否加载成功
    text_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#kw"))
    )
    search_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#su"))
    )
    #
    # # 输入搜索内容 send_keys()
    text_input.send_keys('apple')
    # # 点击搜索按钮 click()
    search_button.click()
    text_input.send_keys('')
    text_input.send_keys('pear')
    search_button.click()



if __name__ == '__main__':
    search(url)
