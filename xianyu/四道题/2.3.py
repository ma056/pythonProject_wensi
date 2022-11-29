# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 2.3.py
@Author : wenjing
@Date : 2022/11/29 15:34
"""
import jieba

excludes = ['那里', '如今', '一个', '我们', '你们', '起来', '姑娘', '这里', '二人', '说道', \
            '知道', '如何', '今日', '什么', '于是', '还有', '出来', '他们', '众人', '奶奶', \
            '自己', '一面', '太太', '只见', '怎么', '两个', '没有', '不是', '不知', '这个', \
            '听见', '这样', '进来', '告诉', '东西', '咱们', '就是', '如此', '回来', '大家', \
            '只是', '老爷', '只得', '丫头', '这些', '不敢', '出去', '所以', '不过', '姐姐', \
            '的话', '不好', '鸳鸯', '一时', '过来', '不能', '心里', '银子', '答应', '几个']
f = open("红楼梦.txt", "r", encoding="utf-8")
# 文件路径
txt = f.read()
f.close()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word in ['宝玉', '宝玉曰', '宝二爷', '绛洞花主', '怡红公子', '宝哥哥', '二哥哥', '宝兄弟', '混世魔王']:
        reword = '贾宝玉'
    elif word in ['黛玉', '黛玉曰', '颦颦', '颦儿', '潇湘妃子', '林姑娘', '林妹妹']:
        reword = '林黛玉'
    elif word in ['宝钗', '宝钗曰', '宝丫头', '宝姐姐', '薛大姑娘', '蘅芜君']:
        reword = '薛宝钗'
    elif word in ['熙凤', '熙凤曰', '琏二奶奶', '凤辣子', '凤哥儿', '凤丫头', '凤姐', '凤姐儿', '琏二嫂子']:
        reword = '王熙凤'
    elif word in ['贾母', '贾母曰', '史太君', '老祖宗', '老太太', '老神仙']:
        reword = '贾母'
    elif word in ['湘云', '湘云曰', '枕霞旧友', '史大姑娘', '云妹妹']:
        reword = '史湘云'
    elif word in ['姨妈', '姨妈曰', '薛夫人', '薛王氏', '姨太太']:
        reword = '贾迎春'
    elif word in ['探春', '探春曰', '玫瑰花', '蕉下客']:
        reword = '贾探春'
    elif word in ['贾珍', '贾珍曰', '珍老爷', '大爷', '大哥哥', '大老爷']:
        reword = '贾珍'
    elif word in ['贾琏', '贾琏曰', '琏二爷', '二爷']:
        reword = '贾琏'
    elif word in ['袭人', '袭人曰', '蕊珠', '花珍珠']:
        reword = '袭人'
    elif word in ['平儿', '平儿曰', '小平', '平姑娘', '平姐姐']:
        reword = '平儿'
    else:
        reword = word
    counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))