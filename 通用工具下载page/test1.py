from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import sys
from pathlib import Path
import html
from urllib.parse import quote


def main(txt_path, out_path):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=service, chrome_options=options)
    browser.maximize_window()
    folder_path = f'{out_path}/PNG1'
    os.makedirs(folder_path, exist_ok=True)
    with open(txt_path, 'r', encoding='utf-8') as fp:
        txt_list = fp.readlines()
        for html_url in txt_list:
            html_url1 = html_url.replace('\n', '')
            # html_url1 = 'https://sell.amazon.com/learn/how-to-sell-books/ess'
            try:
                picture_name = f"{folder_path}/{quote(html_url1.split('://')[1].replace('/',''))}.png"
                browser.get(html_url1)
                # width = browser.execute_script("return document.documentElement.scrollWidth")
                # height = browser.execute_script("return document.documentElement.scrollHeight")
                width = browser.execute_script("return document.body.clientWidth")
                height = browser.execute_script("return document.body.clientHeight")
                browser.set_window_size(width, height)
                time.sleep(1)
                browser.save_screenshot(picture_name)
                time.sleep(4)
            except Exception as e:
                print(f'url:{html_url1}--{e}')


if __name__ == '__main__':
    txt_path = Path(f"{sys.argv[1]}")
    out_path = Path(f"{sys.argv[2]}")
    # txt_path = r'H:/Wenjing/urls.txt'
    # out_path = r'H:/Wenjing/Handback'
    main(txt_path, out_path)