# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : contact.py
@Author : wenjing
@Date : 2022/12/5 11:47
"""
(49, 'a257b013-a7dc-42a5-8f11-51ff70bd7b82', '3', '2', 'true', '59614', '', '1', '', '12135241702', '14133489180',
 '2021-12-01 17:42:58', '227', 1, 'SA', '0', 1, 1, datetime.datetime(2021, 12, 13, 17, 23, 45), 'US', 128.0399932861328,
 217.86000061035156, 'H:\\Projects\\Ring_QA\\Working\\Total\\a257b013-a7dc-42a5-8f11-51ff70bd7b82_1638380648.wav', 1)

id,
contact_id,
environment,
background,
greetingplayed,
oneforma_id,
call_type,
mobile_type,
voip,
system_phone_number,
customer_phone_number,
disconnect_timestamp,
contact_duration,
is_upload,
country,
blob_path,
is_attr_get,
is_search_get,
update_time,
call_center,
speech_length,
audio_length,
audio_path,
is_calculates


# if len(result) > 0:
def create_audio_hit_ring_qa(self, task_name: str, given_data: str, file_url: str,
                             blob_path: str, webapp_id: int, ruleset: str = ""):
    task_id = self.create_task(task_name, webapp_id)
    given_data = self.escape_string(given_data)
    if ruleset == "":
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '', '{blob_path}');"
    else:
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path, ruleset) values ({task_id},'{given_data}', 5, '{file_url}', '', '{blob_path}', '{ruleset}');"
    self.execute_insert_sql(insert_sql)
    return True


def save_new_contact_id_to_engserver(self, contact_id):
    insert_sql = f"insert into contact_info (contact_id) values('{contact_id}');"
    return self.execute_insert_sql_no_wait(insert_sql)


def save_new_call_center_to_engserver(self, id, contact_id, new_attr_json, new_contact_attr_dict, is_upload, country,
                                      blob_path, is_attr_get, is_search_get, update_time, call_center, speech_length,
                                      audio_length, audio_path, is_calculated):
    # new_attr_json = self.escape_string(new_attr_json)
    # new_contact_attr_dict = self.escape_string(new_contact_attr_dict)
    insert_sql = f"insert into call_center (id,contact_id,attr_json,contact_attr_dict,is_upload,country,blob_path,is_attr_get,is_search_get,update_time,call_center,speech_length,audio_length,audio_path,is_calculates) values\
    ({id},'{contact_id}','{new_attr_json}','{new_contact_attr_dict}',{is_upload},'{country}','{blob_path}',{is_attr_get},{is_search_get},'{update_time}','{call_center}',{speech_length},{audio_length},'{audio_path}',{is_calculated});"
    return self.execute_insert_sql_no_wait(insert_sql)





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
                        "attrs": {
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
# get_ringqa_contact_ids              ring_qa_webappid_dict
# save_contact_search_result_to_engserver_call_center         ring_qa_system_phone_dict


def get_country_call_center_phonenumbers(self, attr_system_number):
    select_sql = f"SELECT country FROM call_center_phonenumbers where system_number = {attr_system_number};"
    result = self.execute_select_sql(select_sql)
    if len(result) == 1:
        return result[0][0]
    else:
        return None

def get_webappid_call_center_webapps(self, country):
    select_sql = f"SELECT webappid FROM call_center_webapps where country = {country};"
    result = self.execute_select_sql(select_sql)
    if len(result) == 1:
        return result[0][0]
    else:
        return None
def get_webappid_ids_call_center_webapps(self):
    select_sql = f"SELECT webappid FROM call_center_webapps;"
    result = self.execute_select_sql(select_sql)
    webapp_ids = []
    if len(result) > 0:
        for item in result:
            if item != None:
                webapp_ids.append(item[0])
    return webapp_ids
# 不存在即插入，存在则不做处理
# insert into table(id, name)
# select null, '张三' from DUAL
# where not exists (select id from table where name = '张三') ;

# insert ignore into tt values(1, "aaa"), (2, "bbb"), (3, "ccc");

