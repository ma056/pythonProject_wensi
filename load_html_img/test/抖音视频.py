#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/7/7 3:19 PM 
@process    :
@change :
'''
import os
import urllib.request
import json


def saveHtml(file_name, file_content):
    # 注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        # 写文件用bytes而不是str，所以要转码
        f.write(file_content)


def main():
    json_path = r'Product_batch_3_221121.json'
    with open(json_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
        for html_url in json_data:
            page_url = html_url['page_url']
            html = urllib.request.urlopen(page_url).read()
            saveHtml(page_url.split('/')[-1], html)
            print("下载成功")


if __name__ == '__main__':
    main()
