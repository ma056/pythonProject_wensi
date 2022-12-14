# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 11.py
@Author : wenjing
@Date : 2022/12/2 15:57
"""
temp1 = open(r"C:\Users\Mawenjing\Downloads\file\file\txt\fi_FI _Script(drama,play)_Movies_TV shows_224_20220710.txt",'rb')
file1 = temp1.read()
temp1.close()
temp2 = open(r"C:\Users\Mawenjing\Downloads\file\file\txt\fi_FI _Script(drama,play)_MoviesTV shows_191_20220928.txt",'rb')
file2 = temp2.read
dict1 = {x : file1.count(x) for x in file1}
dict2 = {x : file2.count(x) for x in file2}
similars = set(file1).intersection(set(file2))
rate1 = sum(dict1[w] for w in similars)/len(file1)
rate2 = sum(dict2[w] for w in similars)/len(file2)
print("The rate of similarity is: ", rate1*rate2*100, '%')
print("The similar words are: ", similars)
