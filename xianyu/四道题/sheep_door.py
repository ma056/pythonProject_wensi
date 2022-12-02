# -- coding: utf-8 --
import random
change=0
notchange=0
#time表实验次数
count=eval(input("请输入实验次数："))
for i in range(count):
    car=random.randint(0,2)
    goat=random.randint(0,2)
    if(car==goat):
        change+=1
    else:
        notchange+=1
print("不换门得到汽车的机会：{}".format(change/count))
print("换门得到汽车的机会：{}".format(notchange/count))
