# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 多进程.py
@Author : wenjing
@Date : 2022/112/23 15:49
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

# out_path = r'test'
def main(json_path,out_path):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=service, chrome_options=options)
    browser.maximize_window()
    folder_path = f'{out_path}/HTML'
    os.makedirs(folder_path, exist_ok=True)
    folder_path1 = f'{out_path}/PNG'
    os.makedirs(folder_path1, exist_ok=True)
    with open(json_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
        with ProcessPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(get_data, html_url,folder_path,folder_path1) for html_url in json_data]
            for future in as_completed(futures):
                result = future.result()
                print("in main: get page {}s success".format(result))


def get_data(html_url,folder_path,folder_path1,browser):
    url = html_url['page_url']
    # 下载html
    try:
        f = open(f"{folder_path}/{html_url['id']}.html", 'wb')
        browser.get(url)
        time.sleep(2)
        f.write(browser.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
        f.close()

        # # 截图
        picture_name1 = f"{folder_path1}/{html_url['id']}.png"
        browser.save_screenshot(picture_name1)
        browser.get(url)
        width = browser.execute_script("return document.documentElement.scrollWidth")
        height = browser.execute_script("return document.documentElement.scrollHeight")
        # width1 = browser.execute_script("return document.body.clientWidth")
        # height1 = browser.execute_script("return document.body.clientHeight")

        browser.set_window_size(width, height)
        time.sleep(1)
        browser.save_screenshot(picture_name1)
        time.sleep(4)
        return True
    except Exception as e:
        return False


if __name__ == '__main__':
    # json_path = Path(f"{sys.argv[1]}")
    # out_path = Path(f"{sys.argv[2]}")
    out_path = r'test1'
    json_path = r'Product_task1_10.json'
    main(json_path,out_path)
