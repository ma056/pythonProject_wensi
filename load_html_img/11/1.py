# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 1.py
@Author : wenjing
@Date : 2022/112/23 15:40
"""
import json

with open(r'Product_batch_3_221121.json', 'r', encoding='utf-8') as fp:
    json_data = json.load(fp)
    a = []
    for i in range(0, len(json_data),50):
        b = json_data[i:i + 50]
        a.append(b)
        with open(f"{i}.json", "w") as f:
            f.write(json.dumps(b, ensure_ascii=False))
    # print(b)


    # for html_url in json_data:
    #     print(html_url)