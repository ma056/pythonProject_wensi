# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : DB拆分.py
@Author : wenjing
@Date : 2022/12/7 10:38
"""
import json
a = [1,2]
aa = len(a)
print(aa)

def get_contact_info_not_uploaded_call_center(self):
    try:
        content_dict_list = []
        select_sql = f'''SELECT contact_id, attr_json, contact_attr_json, country, call_center, audio_length, speech_length FROM call_center where is_upload = 0 and is_attr_get = 1 and is_search_get =1 and is_calculated = 1;
        '''
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            for attr_result in result:
                if attr_result != None:
                    attr_contact_id = attr_result[0]
                    attr_attr_json = attr_result[1]
                    attr_contact_attr_json = attr_result[2]
                    attr_country = attr_result[3]
                    attr_call_center = attr_result[4]
                    attr_audio_length = attr_result[5]
                    attr_speech_length = attr_result[6]
                    attr_json_dict = json.loads(attr_attr_json)
                    # {"environment": "3", "background": "2", "greetingplayed": "true", "oneforma_id": "59614",
                    #  "call_type": "", "mobile_type": "1", "voip": ""}
                    # {"System_phone_number": "12135241702", "customer_phone_number": "14133489180",
                    #  "disconnect_timestamp": "2021-12-01 17:42:58", "Contact_duration": "227"}
                    contact_attr_json_dict = json.loads(attr_contact_attr_json)
                    attr_dict = {
                        "contact_id": attr_contact_id,
                        "contact_info": {
                            "contactid": attr_contact_id,
                            "environment": attr_json_dict.get('environment'),
                            "background": attr_json_dict.get('background'),
                            "greetingplayed": attr_json_dict.get('greetingplayed'),
                            "oneforma_id": attr_json_dict.get('oneforma_id'),
                            "call_type": attr_json_dict.get('call_type'),
                            "mobile_type": attr_json_dict.get('mobile_type'),
                            "voip": attr_json_dict.get('voip'),
                            "date": contact_attr_json_dict.get('disconnect_timestamp'),
                            "telephone_number": contact_attr_json_dict.get('customer_phone_number'),
                            "System_phone_number": contact_attr_json_dict.get('System_phone_number'),
                            "Contact_duration": contact_attr_json_dict.get('Contact_duration')[1:],
                        },
                        "country": attr_country,
                        "call_center": attr_call_center,
                        "audio_length": attr_audio_length,
                        "speech_length": attr_speech_length
                    }
                    content_dict_list.append(attr_dict)
        return content_dict_list
    except Exception as e:
        print(e)
        raise