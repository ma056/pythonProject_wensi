from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import json
import sys
from pathlib import Path


def main(json_path, out_path):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=service, chrome_options=options)
    browser.maximize_window()
    # with open(json_path, 'r', encoding='utf-8') as fp:
    #     json_data = json.load(fp)
    #     for html_url in json_data:
    #         url = html_url['page_url']
    url = 'https://tinnitusrecords.com/product/resistance-magazine-19/'
    try:
        folder_path1 = f'{out_path}/PNG'
        os.makedirs(folder_path1, exist_ok=True)
        picture_name1 = f"{folder_path1}/10.png"
        browser.get(url)
        width = browser.execute_script("return document.documentElement.scrollWidth")
        height = browser.execute_script("return document.documentElement.scrollHeight")
        browser.set_window_size(width, height)

        print(width, height)
        time.sleep(1)
        browser.save_screenshot(picture_name1)
        time.sleep(4)
    except Exception as e:
        print(f'url:{url}--{e}')


if __name__ == '__main__':
    # json_path = Path(f"{sys.argv[1]}")
    # out_path = Path(f"{sys.argv[2]}")
    json_path = r'H:/Wenjing/Product_task1_10.json'
    out_path = r'H:/Wenjing/test'
    main(json_path, out_path)