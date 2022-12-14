# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 第一版sql.py
@Author : wenjing
@Date : 2022/12/5 14:20
"""


def get_contact_info(self):
    try:
        content_dict_list = []
        select_sql = f'''SELECT id, contact_id, environment, background, greetingplayed, oneforma_id, call_type, mobile_type, voip, system_phone_number, customer_phone_number, disconnect_timestamp, contact_duration,is_upload, country,blob_path,is_attr_get,is_search_get,update_time, call_center, speech_length,audio_length,audio_path,is_calculated FROM contact_info;
        '''
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            for attr_result in result:
                if attr_result != None:
                    attr_id = attr_result[0]
                    attr_contact_id = attr_result[1]
                    attr_environment = attr_result[2]
                    attr_background = attr_result[3]
                    attr_greetingPlayed = attr_result[4]
                    attr_oneforma_id = attr_result[5]
                    attr_call_type = attr_result[6]
                    attr_mobile_type = attr_result[7]
                    attr_voip = attr_result[8]
                    attr_system_phone_number = attr_result[9]
                    attr_customer_phone_number = attr_result[10]
                    attr_disconnect_timestamp = attr_result[11]
                    attr_contact_duration = attr_result[12]
                    attr_is_upload = attr_result[13]
                    attr_country = attr_result[14]
                    attr_blob_path = attr_result[15]
                    attr_is_attr_get = attr_result[16]
                    attr_is_search_get = attr_result[17]
                    attr_update_time = attr_result[18]
                    attr_call_center = attr_result[19]
                    attr_speech_length = attr_result[20]
                    attr_audio_length = attr_result[21]
                    attr_audio_path = attr_result[22]
                    attr_is_calculated = attr_result[23]

                    attr_dict = {
                        'id': attr_id,
                        "contact_id": attr_contact_id,
                        "attr_json": {
                            "environment": attr_environment,
                            "background": attr_background,
                            "greetingplayed": attr_greetingPlayed,
                            "oneforma_id": attr_oneforma_id,
                            "call_type": attr_call_type,
                            "mobile_type": attr_mobile_type,
                            "voip": attr_voip,
                        },
                        "contact_attr_dict": {
                            "System_phone_number": attr_system_phone_number,
                            "customer_phone_number": attr_customer_phone_number,
                            "disconnect_timestamp": attr_disconnect_timestamp,
                            "Contact_duration": attr_contact_duration,
                        },
                        "is_upload": attr_is_upload,
                        "country": attr_country,
                        "blob_path": attr_blob_path,
                        "is_attr_get": attr_is_attr_get,
                        "is_search_get": attr_is_search_get,
                        "update_time": attr_update_time,
                        "call_center": attr_call_center,
                        "speech_length": attr_speech_length,
                        "audio_length": attr_audio_length,
                        "audio_path": attr_audio_path,
                        "is_calculated": attr_is_calculated
                    }
                    content_dict_list.append(attr_dict)
        return content_dict_list
    except Exception as e:
        print(e)
        raise

def save_new_call_center_to_engserver(self, id, contact_id, new_attr_json, new_contact_attr_dict, is_upload,
                                      country,
                                      blob_path, is_attr_get, is_search_get, update_time, call_center,
                                      speech_length,
                                      audio_length, audio_path, is_calculated):
    # new_attr_json = self.escape_string(new_attr_json)
    # new_contact_attr_dict = self.escape_string(new_contact_attr_dict)
    insert_sql = f"insert into call_center (id,contact_id,attr_json,contact_attr_dict,is_upload,country,blob_path,is_attr_get,is_search_get,update_time,call_center,speech_length,audio_length,audio_path,is_calculates) values\
    ({id},'{contact_id}','{new_attr_json}','{new_contact_attr_dict}',{is_upload},'{country}','{blob_path}',{is_attr_get},{is_search_get},'{update_time}','{call_center}',{speech_length},{audio_length},'{audio_path}',{is_calculated});"
    return self.execute_insert_sql_no_wait(insert_sql)