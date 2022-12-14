# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 111.py
@Author : wenjing
@Date : 2022/12/3 14:56
"""
import jieba
import gensim
import re
import os
import glob
from pathlib import Path
# from FileUtility import CSVOperator


# 获取指定路径的文件内容
def get_file_contents(path):
    string = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:
        string = string + line
        line = f.readline()
    f.close()
    return string


def filter(string):
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = pattern.sub("", string)
    result = jieba.lcut(string)
    return result


def filter2(string):
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = pattern.sub(" ", string)
    string = re.sub(' +', ' ', string)
    result = string.split(' ')
    return result


# 传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text1, text2):
    texts = [text1, text2]
    dictionary = gensim.corpora.Dictionary(texts)
    # vector_way(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim


def vector_way(dictionary):
    # vec1 = [2,4,3,4,5,6,7,8,9]
    # vec2 = [1,2,4,3,4,5,6,7,8,9]
    vec1 = list(dictionary.cfs.keys())
    vec2 = list(dictionary.dfs.keys())
    # print(Cosine(vec1,vec2))


def glob_source_list(base_folder):
    source_list = []
    extensions = ['txt']
    for extension in extensions:
        source_list.extend(
            glob.glob(f"{base_folder}/**/*.{extension}", recursive=True))
    print(f"{len(source_list)} files found")
    return source_list


def main_test():
    folder_path = Path(r"C:\Users\Mawenjing\Downloads\file\file\txt")
    source_list = glob_source_list(folder_path)
    if len(source_list) < 2:
        return
    written_lines = []
    for i in range(len(source_list)):
        if i + 1 == len(source_list):
            break
        for j in range(i + 1, len(source_list)):
            # if i +1 ==len(source_list):
            #     break
            t_dict = {}
            path1 = source_list[i]
            path2 = source_list[j]
            str1 = get_file_contents(path1)
            str2 = get_file_contents(path2)
            text1 = filter2(str1)
            text2 = filter2(str2)
            similarity = calc_similarity(text1, text2)
            result = round(similarity.item(), 5)
            t_dict['path1'] = path1
            t_dict['path2'] = path2
            t_dict['result'] = result
            written_lines.append(t_dict)
            print(i,j)
            print(result)
    # output_path = Path(f"H:/PipelineFTP/Temp")
    # output_path.mkdir(parents=True, exist_ok=True)
    # csv_path = output_path.joinpath(f"d_{strnowforfilename()}.csv")
    # csvo = CSVOperator(csv_path)
    # csvo.dict_to_csv(written_lines)


if __name__ == '__main__':
    main_test()
