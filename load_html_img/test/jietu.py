# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : jietu.py
@Author : wenjing
@Date : 2022/112/22 16:53
"""
from selenium import webdriver
from PIL import Image
from time import sleep
import time


def test1():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=service, chrome_options=options)

    # browser = webdriver.Chrome()
    # 打开一个注册界面
    browser.get('https://www.wundermittel.store/cbd-oel-kostenlos-ausprobieren/')
    # 最大化浏览器
    browser.maximize_window()
    # 下面三行是为截图加上时间
    picture_name1 = 'H:/Wenjing/test/img/a.png'
    # 下面一行为保存整个页面的截图
    browser.save_screenshot(picture_name1)
