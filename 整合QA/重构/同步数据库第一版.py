# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 同步数据库第一版.py
@Author : wenjing
@Date : 2022/12/5 14:19
"""
import sys
from pathlib import Path
sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
import DBUtility as dbu
from DBUtility import OneForma
import json

dbo = OneForma("RINGQA")
def main():
    # eng_db = dbu.OneForma("RINGQA")
    # contact_info_in_engserver = dbo.get_contact_info_from_engserver()
    # for info in contact_info_in_engserver:
    #     print(info)
    #     print("==="*30)
    upload_dict_list = dbo.get_contact_info()
    if len(upload_dict_list) <= 0:
        print("No task need to upload")
        return
    # for i in range(0, len(upload_dict_list)):
    for i in range(0, 4):
        try:
            upload_dict = upload_dict_list[i]
            id = upload_dict['id']
            contact_id = upload_dict['contact_id']
            attr_json = upload_dict["attr_json"]
            contact_attr_dict = upload_dict["contact_attr_dict"]
            is_upload = upload_dict['is_upload']
            country = upload_dict['country']
            blob_path = upload_dict['blob_path']
            is_attr_get = upload_dict['is_attr_get']
            is_search_get = upload_dict['is_search_get']
            update_time = upload_dict['update_time']
            call_center = upload_dict['call_center']
            speech_length = upload_dict['speech_length']
            audio_length = upload_dict['audio_length']
            audio_path = upload_dict['audio_path']
            is_calculated = upload_dict['is_calculated']
            new_attr_json = json.dumps(attr_json)
            new_contact_attr_dict = json.dumps(contact_attr_dict)

            dbo.save_new_call_center_to_engserver(id,contact_id,new_attr_json,new_contact_attr_dict,is_upload,country,blob_path,is_attr_get,is_search_get,update_time,call_center,speech_length,audio_length,audio_path,is_calculated)
        except Exception as e:
            print(e)
            raise

main()