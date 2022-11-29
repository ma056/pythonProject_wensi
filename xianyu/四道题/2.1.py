# -- coding: utf-8 --
names = "宝玉、林黛玉、薛宝钗、贾元春、贾迎春、贾探春、贾惜春、李纨、妙玉、史湘云、王熙凤、贾巧姐、秦可卿、晴雯、麝月、袭人、鸳鸯、雪雁、紫鹃、碧痕、平儿、香菱、金钏、司棋、抱琴、赖大、焦大、王善保、周瑞、林之孝、乌进孝、包勇、吴贵、吴新登、邓好时、王柱儿、余信、庆儿、昭儿、兴儿、隆儿、坠儿、喜儿、寿儿、丰儿、住儿、小舍儿、李十儿、玉柱儿、贾敬、贾赦、贾政、贾宝玉、贾琏、贾珍、贾环、贾蓉、贾兰、贾芸、贾蔷、贾芹、琪官、芳官、藕官、蕊官、药官、玉官、宝官、龄官、茄官、艾官、豆官、葵官、妙玉、智能、智通、智善、圆信、大色空、净虚、彩屏、彩儿、彩凤、彩霞、彩鸾、彩明、彩云、贾元春、贾迎春、贾探春、贾惜春、贾宝玉、甄宝玉、薛宝钗、薛宝琴、薛蟠、薛蝌、薛宝钗、薛宝琴、王夫人、王熙凤、王子腾、王仁、尤老娘、尤氏、尤二姐、尤三姐、贾蓉、贾兰、贾芸、贾芹、贾珍、贾琏、贾环、贾瑞、贾敬、贾赦、贾政、贾敏、贾代儒、贾代化、贾代修、贾代善、詹光、单聘仁、程日兴、王作梅、石呆子、张华、冯渊、张金哥、茗烟、扫红、锄药、伴鹤、小鹊、小红、小蝉、小舍儿、刘姥姥、马道婆、宋嬷嬷、张妈妈、秦锺、蒋玉菡、柳湘莲、东平王、乌进孝、冷子兴、山子野、方椿、载权、夏秉忠、周太监、裘世安"
print(names)
names = names.split('、')

import jieba

with open('红楼梦.txt', "r", encoding='utf-8') as file:
    txt = file.read()
words = jieba.lcut(txt)
cnt = {}  # 用来计数
for word in words:
    if word not in names:  # 如果根本不是人名，那就不记录这个分词了
        continue
    cnt[word] = cnt.get(word, 0) + 1
items = list(cnt.items())  # 将其返回为列表类型
items.sort(key=lambda x: x[1], reverse=True)  # 排序
for i in range(20):  # 输出我亲爱得二维列表
    name, ans = items[i]
    print("{0:<5}出现次数为：{1:>5}".format(name, ans))
