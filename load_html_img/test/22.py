# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 22.py
@Author : wenjing
@Date : 2022/11/23 14:14
"""
# -*- coding: utf-8 -*-
import requests
from lxml import etree
import re
import os

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

onpath = os.getcwd()


# 获取网页资源
def getsourceweb(weburl, type):
    r = requests.get(weburl, headers=header)
    # 获取js
    if type == 'js':
        return getsourcejs(r.text)
    elif type == 'css':
        # 获取css
        return getsourcecss(r.text)


# 获取js资源的name、 url
def getsourcejs(source):
    print("获取JS资源：-------------")
    if os.path.exists(onpath + "/js"):
        pass
    else:
        os.mkdir(onpath + "/js")
    res = re.findall("<script src=\'(.*?)\'></script>", source, re.S)

    jssource = []
    for url in res:
        jslist = url.split("/")
        jsname = re.findall("(.*?)\?", jslist[-1])
        js = {'url': url, 'name': jsname[0]}
        jssource.append(js)
    print("共获取{}个js文件".format(len(jssource)))
    return savesource(jssource, 'js')


# 获取css资源的name 、url
def getsourcecss(source):
    print("获取CSS资源：-------------")
    if os.path.exists(onpath + "/css"):
        pass
    else:
        os.mkdir(onpath + "/css")
    res = re.findall("<link.*?href=\'(.*?)\' media=\'all\' />", source, re.S)
    csssource = []
    for url in res:
        csslist = url.split("/")
        cssname = re.findall("(.*?)\?", csslist[-1])
        if ".css" in cssname[0]:
            css = {'url': url, 'name': cssname[0]}
            csssource.append(css)
    print("共获取{}个css文件".format(len(csssource)))
    return savesource(csssource, 'css')


# 保存资源到本地 并创建文件
def savesource(sourcelist, type):
    jspath = onpath + os.path.join('/') + os.path.join(type)
    print(jspath)
    os.chdir(jspath)
    for i, s in enumerate(sourcelist):
        source_url = s['url']
        souce_name = s['name']
        print(s)
        if i > 0:
            r = requests.get(source_url)
            with open(str(souce_name), "wb") as code:
                code.write(r.content)
                print("{}保存成功！".format(souce_name))


# 保存网页
def savewebhtml(url, name):
    r = requests.get(url)
    with open(str(name), "wb") as code:
        code.write(r.content)


if __name__ == '__main__':
    print("start------------------")

    # print(os.path.exists(onpath+"/js"))
    # 保存网页
    savewebhtml("https://defenseinnovation.com/products/universal-hoslter-glock-s-w-sig-sauer-walther-ruger-1911-and-others-left-right-hand","home.html")

    # 保存js和css
    getsourceweb("https://defenseinnovation.com/products/universal-hoslter-glock-s-w-sig-sauer-walther-ruger-1911-and-others-left-right-hand", "js")
    getsourceweb("https://defenseinnovation.com/products/universal-hoslter-glock-s-w-sig-sauer-walther-ruger-1911-and-others-left-right-hand", "css")

print("end------------------")

