from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import base64
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(service=service, chrome_options=options)

# get_html = "H:/Wenjing/test/img/test.html"
# #打开文件，准备写入
# f = open(get_html,'wb')
# url = 'https://greatawakeningglobalcommunity.com/'
# browser.get(url)
# time.sleep(2) # 保证浏览器响应成功后再进行下一步操作
# #写入文件
# f.write(browser.page_source.encode("gbk", "ignore")) # 忽略非法字符
# print('写入成功')
# f.close()
#
#


# 最大化浏览器
browser.maximize_window()
# sizeDict=browser.get_window_size()
# 下面三行是为截图加上时间
picture_name1 = 'H:/Wenjing/test/img/a1.png'
# 下面一行为保存整个页面的截图
browser.save_screenshot(picture_name1)
browser.get('https://www.ginetteetjosiane.com/librairie?add-to-cart=9566')
width = browser.execute_script("return document.body.clientWidth")
height = browser.execute_script("return document.body.clientHeight")

# h1 = browser.execute_script("return window.screen.availWidth")
# h2 = browser.execute_script("return window.outerWidth;")
# h3 = browser.execute_script("return document.body.offsetWidth")
# h4 = browser.execute_script("return document.body.scrollWidth")
browser.set_window_size(1366, height)
time.sleep(1)
browser.save_screenshot(picture_name1)
browser.close()


# width = browser.execute_script("return document.body.scrollWidth")
# height = browser.execute_script("return document.body.scrollHeight")
# browser.get('https://www.ginetteetjosiane.com/librairie?add-to-cart=9566')
# browser.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {'mobile':False, 'width':800, 'height':1000, 'deviceScaleFactor': 1})
# # 执行截图
# res = browser.execute_cdp_cmd('Page.captureScreenshot', { 'fromSurface': True})
# # 返回的base64内容写入PNG文件
# with open('H:/Wenjing/test/img/a2.png', 'wb') as f:
#     img = base64.b64decode(res['data'])
#     f.write(img)
# # 等待截图完成
# time.sleep(15)
# # 关闭设备模拟
# browser.execute_cdp_cmd('Emulation.clearDeviceMetricsOverride', {})
