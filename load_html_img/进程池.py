# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 多进程.py
@Author : wenjing
@Date : 2022/11/23 15:49
"""

import os
import json
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

out_path = r'test'
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
    print(url)
    return url


if __name__ == '__main__':
    # json_path = Path(f"{sys.argv[1]}")
    # out_path = Path(f"{sys.argv[2]}")
    out_path = r'test'
    json_path = r'Product_task1_10.json'
    main(json_path)
