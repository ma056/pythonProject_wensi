from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(service=service, chrome_options=options)

get_html = "H:/Wenjing/test/img/test.html"
#打开文件，准备写入
f = open(get_html,'wb')
url = 'https://greatawakeningglobalcommunity.com/'
browser.get(url)
time.sleep(2) # 保证浏览器响应成功后再进行下一步操作
#写入文件
f.write(browser.page_source.encode("gbk", "ignore")) # 忽略非法字符
print('写入成功')
f.close()
