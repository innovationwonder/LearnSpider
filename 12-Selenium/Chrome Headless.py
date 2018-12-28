from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://www.baidu.com'
browser.get(url)
print(browser.current_url)