# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : count_person_num.py
@Author : wenjing
@Date : 2022/11/29 14:43
"""
import jieba

excludes = {'什么', '一个', '我们', '你们', '如今', '说道', '知道', '起来', '这里', '奶奶',
            '姑娘', '出来', '众人', '那里', '自己', '他们', '一面', '只见', '怎么', '老太太',
            '两个', '没有', '不是', '不知', '这个', '听见', '这样', '进来', '咱们', '太太',
            '告诉', '就是', '东西', '回来', '只是', '大家', '只得', '丫头', '姐姐', '不用',
            '过来', '心里', '如此', '今日', '这些', '不敢', '出去', '所以', '不过', '的话',
            '不好', '一时', '不能', '银子', '几个', '答应', '二人', '还有', '只管', '这么',
            '说话', '一回', '那边', '这话', '外头', '打发', '自然', '今儿', '罢了', '屋里',
            '那些', '听说', '如何', '问道', '看见', '二爷', '小丫头', '人家', '妹妹', '老爷'}
txt = open("红楼梦.txt", "r", encoding='utf-8').read()
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
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print("{0:{2}<10}{1:{2}>5}".format(word, count, chr(12288)))
