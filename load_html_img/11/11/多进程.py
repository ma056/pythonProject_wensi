# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 多进程.py
@Author : wenjing
@Date : 2022/11/23 15:49
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import json
import sys
from pathlib import Path


from concurrent.futures import ProcessPoolExecutor, as_completed
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(service=service, chrome_options=options)
browser.maximize_window()
out_path = r'H:/Wenjing/100'


def main(json_path):
    with open(json_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
        with ProcessPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(get_data, html_url) for html_url in json_data]
            for future in as_completed(futures):
                result = future.result()
                print("in main: get page {}s success".format(result))


def get_data(html_url):
    url = html_url['page_url']
    folder_path = f'{out_path}/HTML'
    os.makedirs(folder_path, exist_ok=True)

    # # 写入html文件
    try:
        f = open(f"{folder_path}/{html_url['id']}.html", 'wb')
        browser.get(url)
        time.sleep(2)
        f.write(browser.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
        f.close()

        # # 截图
        folder_path1 = f'{out_path}/PNG'
        os.makedirs(folder_path1, exist_ok=True)
        picture_name1 = f"{folder_path1}/{html_url['id']}.png"
        browser.save_screenshot(picture_name1)
        browser.get(url)
        width = browser.execute_script("return document.documentElement.scrollWidth")
        height = browser.execute_script("return document.documentElement.scrollHeight")

        browser.set_window_size(width, height)
        time.sleep(1)
        browser.save_screenshot(picture_name1)
        time.sleep(4)
    except Exception as e:
        print(f'url:{url}--{e}')


if __name__ == '__main__':
    # json_path = Path(f"{sys.argv[1]}")
    # out_path = Path(f"{sys.argv[2]}")
    json_path = r'H:/Wenjing/100.json'
    main(json_path)
