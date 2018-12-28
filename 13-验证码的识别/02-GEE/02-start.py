'''
1.模拟点击按钮
    使用 selenium 点击按钮
2.识别滑动缺口的位置
    实现一个边缘检测算法：通过获取原图和有缺口的图 设置对比阈值，相同位置 RGB 差距超过此阈值的像素点时缺口的位置
3.模拟拖动滑块
    模拟人的移动轨迹才可通过，即 先加速后减速
'''
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化
EMALL = 'hyyh10@163.com'
PASSWORD = 'GEE25546795'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://acount.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMALL
        self.password = PASSWORD

    # 模拟点击
    def get_geetest_button(self):
        """获取验证码验证按钮
        return 按钮对象"""
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    # 识别缺口
    def get_srcrenshot(self):
        """获取网页截图，
        return 截图对象"""
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        """获取验证码位置
        return 验证码位置元祖h"""
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_radar_tip')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']

        return (top, bottom, left, right)

    def get_img(self, name='captchab.png'):
        """获取验证码图片
        :return 图片对象"""
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_srcrenshot()
        captahab = screenshot.crop((left, top, right, bottom)) # 调用 crop 方法将图片裁切出来
        return captahab

    def get_slider(self):
        """获取滑块
        :return 滑块对象"""
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider
