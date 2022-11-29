# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 2.2.py
@Author : wenjing
@Date : 2022/11/29 15:14
"""
import jieba
txt = open("红楼梦.txt","r",encoding = 'utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "宝玉" or word == "宝二爷":
        rword = "贾宝玉"
    elif word == "凤姐" or word == "凤辣子" or word == "凤姐儿" or word == "琏二奶奶" or word == "凤丫头" or word == "凤哥儿":
        rword = "王熙凤"
    elif word == "老祖宗" or word == "老太君":
        rword = "贾母"
    elif word == "颦颦" or word == "林姑娘" or word == "黛玉" or word == "林妹妹" or word == "潇湘妃子" or word == "林丫头":
        rword = "林黛玉"
    elif word == "宝姑娘" or word == "宝丫头" or word == "蘅芜君" or word == "宝姐姐" or word == "宝钗":
        rword = "薛宝钗"
    elif word == "湘云":
        rword = "史湘云"
    elif word == "存周":
        rword = "贾政"
    elif word == "花珍珠" or word == "花大姑娘":
        rword = "袭人"
    else:
        rword = word

    counts[rword] = counts.get(rword,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
