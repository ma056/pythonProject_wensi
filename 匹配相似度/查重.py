# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 查重.py
@Author : wenjing
@Date : 2022/12/5 9:49
"""
import glob
from fuzzywuzzy import fuzz
from itertools import combinations
import Path
from FileUtility import CSVOperator

def main(txt_paths):
    txt_paths_list = []
    res_paths_list = glob.glob(f'{txt_paths}/*.txt', recursive=True)
    txt_paths_list.extend(res_paths_list)
    comb = combinations(txt_paths_list, 2)
    res_list = []
    for i in list(comb):
        # print(''.join(map(str, i)))
        # a.append('------'.join(map(str, i)))
        res_dict = {}
        with open(i[0], 'rb') as f:
            first_txt_list = []
            for i1 in f.readlines():
                first_txt_list.append(i1)
        with open(i[1], 'rb') as f:
            second_txt_list = []
            for i2 in f.readlines():
                second_txt_list.append(i2)
        rep_rate = fuzz.token_set_ratio(first_txt_list, second_txt_list)
        res_dict['first_path'] = i[0]
        res_dict['second_path'] = i[1]
        res_dict['rep_rate'] = rep_rate
        res_list.append(res_dict)
        print(f'{i[0]}----{i[1]}----{rep_rate}')
    output_path = Path(f"H:/PipelineFTP/Temp")
    output_path.mkdir(parents=True, exist_ok=True)
    csv_path = output_path.joinpath("res_data.csv")
    csvo = CSVOperator(csv_path)
    csvo.dict_to_csv(res_list)


if __name__ == '__main__':
    txt_paths = r'C:\Users\Mawenjing\Downloads\file\file\txt'
    main(txt_paths)
