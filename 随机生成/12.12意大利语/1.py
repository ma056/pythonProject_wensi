# -- coding: utf-8 --
country=[]
with open("country.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
    for i in content:
        print(i)
#         a = str(i)
        country.append(str(i))
# print(country)country