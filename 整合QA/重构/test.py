# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test.py
@Author : wenjing
@Date : 2022/12/7 13:33
"""
import sys
from pathlib import Path
sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
import html
# from Utilities.DatetimeUtility import strtoday


def main():
    dbo = OneForma("RINGQA")
    # eng_db = dbu.OneForma("RINGQA")
    upload_dict_list = dbo.get_contact_info_not_uploaded()
    upload_dict_list1 = dbo.get_contact_info_not_uploaded_call_center()
    print(len(upload_dict_list))
    print(len(upload_dict_list1))
    print(upload_dict_list1)

if __name__ == "__main__":
    # # webappids = sys.argv[1]
    # # webappids = '3848'
    # if webappids[-1] == ",":
    #     webappids = webappids[:-1]
    # webappid_list = webappids.split(",")

    # main(webappid_list,webappids)
    main()
