# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 3.py
@Author : wenjing
@Date : 2022/12/2 16:27
"""
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
data = fuzz.token_set_ratio([1,'sas'],['sa',1])
data1 = fuzz.token_set_ratio('UP 093 käsikirjoitus final: "Kylläs ryypyn otat kun leskeks jäät." Jaksoesittelyteksti ','71. TYTÖN HUONE/ILTANuorko tyttö laittaa Irwinin levyn levysoittimeen, katselee seinälle,')
print(data,data1)