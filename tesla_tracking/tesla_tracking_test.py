# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : tesla_tracking_test.py
@Author : wenjing
@Date : 2022/11/17 16:44


"""

import os
import pandas as pd

def process(excel_paths,holiday_paths):
    df = pd.read_excel(excel_paths,sheet_name=None)
    a = df.keys()
    print(a)
    # for file_name in os.listdir(holiday_paths):
    #     print(file_name)
    #     path =os.path.join(holiday_paths,file_name)
    #     df = pd.read_csv(path,sheet_name=None)
    #     # target_locale = df['Target Locale'][0]
    #     # a = f"'{file_name}"
    #     aa = df.sheet.name
    #     print(df)


if __name__ == '__main__':
    excel_paths = r"C:\Users\Mawenjing\Desktop\data\task\Tesla_Tracking_20221111.xlsm"
    holiday_paths = r'C:\Users\Mawenjing\Desktop\data\11.11 holiday'
    process(excel_paths,holiday_paths)
