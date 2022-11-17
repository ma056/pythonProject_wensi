from operator import and_
from DatetimeUtility import *
import json, pymysql, uuid
from enum import Enum
import ConstConfig as config
import mysql5.mysql.connector as mysql5conn
import mysql8.mysql.connector as mysql8conn
from dbutils.pooled_db import PooledDB
from dbutils.persistent_db import PersistentDB
import hashlib


# Bacis Enum setting for Database
class DB_type(Enum):
    Default = 0
    SQlite = 1
    Mysql = 2


class DB_Name(Enum):
    Default = 0
    Oneforma_Main = 3
    Oneforma_Test = 4
    Oneforma_Asia = 5
    OneForma_Local = 6
    PowerBi_Main = 7
    PowerBi_Local = 8
    Oneforma_API = 9
    EngServer = 10
    RingQA = 2
    HeliosEng = 11
    OneForma_Local_Eng = 12
    TencentTestDB = 13
    Oneforma_VPN = 14


# Basic DB Class
class DBOperator:
    def __init__(self, db_name: DB_Name):
        self.db_name = db_name
        self.is_open = False
        self.db_type = DB_type.Default
        self.pool = None
        self.single_insert_limit = 500
        self.insert_count = 0
        self.insert_sleep_time = 1

    def __del__(self):
        if self.pool != None and self.db_type == DB_type.Mysql:
            self.pool.close()
        pass

    def escape_string(self, input_str):
        return pymysql.converters.escape_string(input_str)

    ## Open database via db Name
    def open_database(self):
        # print(self.db_name)
        try:
            if self.db_name == DB_Name.Oneforma_Main:
                self.pool = PooledDB(
                    mysql8conn,
                    maxconnections=5,
                    host="oneformadbnew.mysql.database.azure.com",
                    port=3306,
                    user="engineering",
                    passwd="&d&K9VrUE6l3e^Jp",
                    database="scribo_webapps_db")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.Oneforma_VPN:
                self.pool = PooledDB(mysql8conn,
                                     maxconnections=5,
                                     host="10.3.0.4",
                                     port=3306,
                                     user="yixiang@oneformaserver2",
                                     passwd="newpass219",
                                     database="scribo_webapps_db")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.Oneforma_Test:
                self.pool = PooledDB(mysql8conn,
                                     maxconnections=10,
                                     host="engserver.westus.cloudapp.azure.com",
                                     port=3306,
                                     user="bi_report",
                                     passwd="pass@123",
                                     database="Oneforma_local")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.Oneforma_Asia:
                self.pool = PooledDB(
                    mysql8conn,
                    maxconnections=10,
                    host="oneformaelastic2.mysql.database.azure.com",
                    port=3306,
                    user="engbi3@oneformaelastic2",
                    password="engbi@220",
                    database="scribo_webapps_db")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.OneForma_Local:
                self.pool = PooledDB(mysql8conn,
                                     maxconnections=10,
                                     host="localhost",
                                     port=3306,
                                     user="root",
                                     password="rootroot",
                                     database="Oneforma_local")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.OneForma_Local_Eng:
                self.pool = PooledDB(mysql8conn,
                                     maxconnections=10,
                                     host="localhost",
                                     port=3306,
                                     user="root",
                                     password="pass@123",
                                     database="Oneforma_local")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.PowerBi_Main:
                self.pool = PooledDB(
                    mysql8conn,
                    maxconnections=2,
                    host="engserver.westus.cloudapp.azure.com",
                    port=3306,
                    user="bi_report",
                    password="pass@123",
                    database="bi_new")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.PowerBi_Local:
                self.pool = PooledDB(mysql8conn,
                                     maxconnections=10,
                                     host="localhost",
                                     port=3306,
                                     user="root",
                                     password="pass@123",
                                     database="bi_new")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.Oneforma_API:
                self.pool = PooledDB(mysql8conn,
                                     maxconnections=10,
                                     host="localhost",
                                     port=3306,
                                     user="root",
                                     password="rootroot",
                                     database="Oneforma_API")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.EngServer:
                self.pool = PooledDB(mysql8conn,
                                     maxconnections=10,
                                     host="localhost",
                                     port=3306,
                                     user="bi_report",
                                     password="pass@123",
                                     database="Oneforma_API")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.RingQA:
                self.pool = PooledDB(
                    mysql8conn,
                    maxconnections=10,
                    host="engserver.westus.cloudapp.azure.com",
                    port=3306,
                    user="bi_report",
                    password="pass@123",
                    database="helios")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.HeliosEng:
                self.pool = PooledDB(
                    mysql8conn,
                    maxconnections=10,
                    host="localhost",
                    port=3306,
                    user="bi_report",
                    password="pass@123",
                    database="helios")
                self.db_type = DB_type.Mysql
            elif self.db_name == DB_Name.TencentTestDB:
                self.pool = PooledDB(
                    mysql8conn,
                    maxconnections=10,
                    host="118.195.205.252",
                    port=3306,
                    user="andrew",
                    password="Idothink926!",
                    database="helios")
                self.db_type = DB_type.Mysql
            else:
                print("No DB setting exies")
                return False
            return True
        except Exception as e:
            print(e)
            return False

    ## Execute Sql
    def execute_select_sql(self, sql):
        if self.pool != None:
            conn = self.pool.connection()
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(e)
                raise
            finally:
                conn.close()
        else:
            print("DB pool not created")
            raise

    def execute_select_sql_to_dict_list(self, sql):
        if self.pool != None:
            conn = self.pool.connection()
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(e)
                raise
            finally:
                conn.close()
        else:
            print("DB pool not created")
            raise

    def execute_insert_sql(self, sql):
        self.insert_count += 1
        if self.insert_count % self.single_insert_limit == 0 and self.insert_count >= self.single_insert_limit:
            print("Sleep")
            sleep(self.insert_sleep_time)
        if self.pool != None:
            conn = self.pool.connection()
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(sql)
                print(e)
                raise
            finally:
                conn.close()
        else:
            print("DB pool not created")
            raise

    def execute_insert_sql_no_wait(self, sql):
        if self.pool != None:
            conn = self.pool.connection()
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(sql)
                print(e)
                raise
            finally:
                conn.close()
        else:
            print("DB pool not created")
            raise

    def execute_insert_sql_no_wait_ret_id(self, sql):
        if self.pool != None:
            conn = self.pool.connection()
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                ret_id = cursor.lastrowid
                conn.commit()
                cursor.close()
                return ret_id
            except Exception as e:
                print(sql)
                print(e)
                raise
            finally:
                conn.close()
        else:
            print("DB pool not created")
            raise


class OneForma(DBOperator):
    def __init__(self, usage: str):
        if usage.upper() == "TEST":
            super().__init__(DB_Name.Oneforma_Test)
        elif usage.upper() == "MAIN":
            super().__init__(DB_Name.Oneforma_Main)
        elif usage.upper() == "ASIA":
            super().__init__(DB_Name.Oneforma_Asia)
        elif usage.upper() == "LOCAL":
            super().__init__(DB_Name.OneForma_Local)
        elif usage.upper() == "ENG_LOCAL":
            super().__init__(DB_Name.OneForma_Local_Eng)
        elif usage.upper() == "API":
            super().__init__(DB_Name.Oneforma_API)
        elif usage.upper() == "RINGQA":
            super().__init__(DB_Name.RingQA)
        elif usage.upper() == "VPN":
            super().__init__(DB_Name.Oneforma_VPN)
        else:
            print("Other usage is not supported")
            raise
        self.is_open = self.open_database()
        self.uploader = "ENG"

    def insert(self, table_name: str, data_dict: dict):
        # { "data_handled":"1111"}
        table_keys = ""
        table_values = ""
        for key, value in data_dict.items():
            table_keys += f"`{key}`,"
            table_values += f"'{value}',"
        table_keys = table_keys[:-1]
        table_values = table_values[:-1]
        insert_sql = "INSERT INTO " + table_name + "(" + table_keys + ") VALUES(" + table_values + ");"
        return self.execute_insert_sql(insert_sql)



    def create_silver_task(self,
                           task_name: str,
                           webapp_id: int,
                           is_exam=False) -> int:
        task_name = self.escape_string(task_name)
        select_sql = f"select taskid from silvertask where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            if is_exam:
                insert_sql = f"insert into silvertask (webappid, taskname, uploader, internal_taskname, upload_date, status, exam_task) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}','3', 1);"
            else:
                insert_sql = f"insert into silvertask (webappid, taskname, uploader, internal_taskname, upload_date, status) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}','3');"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from silvertask where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    def create_hit_metadata(self, hitid: int, meatdata: str):
        insert_sql = f"replace into hit_metadata (HitID, metadata) values ({hitid},'{meatdata}');"
        self.execute_insert_sql(insert_sql)

    ## for Ring QA
    def assign_task_to_user(self, task_id, judge_id, assign_number):
        insert_sql = f"insert into task_assignments (task_id, judge_id, current, `limit`) values ({task_id},{judge_id},0,{assign_number});"
        self.execute_insert_sql(insert_sql)
        return True

    def create_txt_hits_multi_with_audio_length(self,
                                                task_name,
                                                fileurl,
                                                given_data: str,
                                                webapp_id,
                                                audio_length,
                                                multi=3):
        task_id = self.create_task(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql(insert_sql)
            if multi != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")
        select_sql = f"select hitid from tasks_hits where FileURL = '{fileurl}' and taskid = {task_id};"
        result = self.execute_select_sql(select_sql)
        if len(result) == multi:
            for hitid in result:
                hitid = hitid[0]
                replace_sql = f"replace into hit_metadata (HitID, metadata) values ({hitid},'{audio_length}');"
                self.execute_insert_sql(replace_sql)
        else:
            print(f"{fileurl} multi hit error")

    def create_txt_hits_multi_with_audio_length_grace(self,
                                                      task_name,
                                                      fileurl,
                                                      given_data: str,
                                                      webapp_id,
                                                      audio_length,
                                                      multi=3):
        task_id = self.create_task_all_limited(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql(insert_sql)
            # if multi != 1:
            #     print(f"{task_name} --- Create hit {str(i+1)} times --- Done")
        select_sql = f"select hitid from tasks_hits where FileURL = '{fileurl}' and taskid = {task_id};"
        result = self.execute_select_sql(select_sql)
        if len(result) == multi:
            for hitid in result:
                hitid = hitid[0]
                replace_sql = f"replace into hit_metadata (HitID, metadata) values ({hitid},'{audio_length}');"
                self.execute_insert_sql(replace_sql)
        else:
            print(f"{fileurl} multi hit error")

    def create_silver_txt_hits(self,
                               task_name,
                               given_data: str,
                               solution: str,
                               webapp_id,
                               hits_limit=1,
                               ruleset: str = "",
                               fileurl: str = "",
                               is_exam=False):
        if is_exam:
            task_id = self.create_silver_task(task_name, webapp_id, True)
        else:
            task_id = self.create_silver_task(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        solution = self.escape_string(solution)
        hlmd5 = hashlib.md5()
        hlmd5.update(fileurl.encode('utf-8'))
        internal_filename = hlmd5.hexdigest()
        for i in range(0, hits_limit):
            insert_sql = f"insert into silverhits (taskid, given_data, solution,internal, FileURL, internal_filename, ruleset) values ({task_id},'{given_data}','{solution}', 1, '{fileurl}', '{internal_filename}','{ruleset}');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")


    def get_task_word_count_by_id(self, task_id: int):
        select_sql = f"select metadata from task_metadata where taskid = '{task_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]



    def get_not_finished_hits_by_task_id(self, task_id: int) -> int:
        select_sql = f"select count(HitID) from scribo_webapps_db.tasks_hits where taskid = {task_id} and data_handled is NULL;"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]



    def get_webapp_name_by_webapp_id(self, webapp_id):
        select_sql = f"select webapp_name from `corpus2_db`.`webapps` where id = '{webapp_id}';"
        result = self.execute_select_sql(select_sql)
        if result is not None:
            return result[0][0]
        else:
            return None

    def get_webapp_locale_by_webapp_id(self, webapp_id):
        select_sql = f"select locale from `corpus2_db`.`webapps` where id = '{webapp_id}';"
        result = self.execute_select_sql(select_sql)
        if result is not None:
            return result[0][0]
        else:
            return None

    def get_taskgroup_name_by_webapp_id(self, webapp_id):
        select_sql = f"select taskgroup_name from `taskgroups` where webapp_id = '{webapp_id}';"
        result = self.execute_select_sql(select_sql)
        if result is not None:
            return result[0][0]
        else:
            return None

    def get_taskgroup_id_by_name(self, taskgroup_name):
        select_sql = f"select ID, webapp_id from `taskgroups` where taskgroup_name = '{taskgroup_name}';"
        result = self.execute_select_sql(select_sql)
        if result is not None and len(result) > 0:
            return result[0][0]
        else:
            return None

    def create_taskgourp(self, taskgroup_name, webappid):
        insert_sql = f"insert into `taskgroups` (taskgroup_name, webapp_id) values ('{taskgroup_name}', '{webappid}');"
        return self.execute_insert_sql_no_wait_ret_id(insert_sql)

    def get_user_id_by_done_by(self, done_by):
        select_sql = f"select id from corpus2_db.users_auth where username = '{done_by}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_agency_id_by_user_id(self, user_id):
        select_sql = f"select vendor_id from corpus2_db.users_agencies_info where resource_id = '{user_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_agency_name_by_agency_id(self, agency_id):
        select_sql = f"select agency_name from corpus2_db.agencies_search where agency_id = '{agency_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_user_id_by_employeeid(self, employee_id):
        select_sql = f"select resource_id from corpus2_db.users_employees_info where employee_id = '{employee_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_hit_metadata_by_hit_id(self, hitid):
        select_sql = f"select metadata from hit_metadata where hitid = '{hitid}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_task_assignments_by_task_id(self, taskid):
        select_sql = f"select id from task_assignments where task_id = '{taskid}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result
        else:
            return None

    def get_task_assignments_judge_id_by_task_id(self, taskid):
        select_sql = f"select judge_id from task_assignments where task_id = '{taskid}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_task_assignments_current_by_task_id(self, taskid):
        select_sql = f"select current from task_assignments where task_id = '{taskid}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result
        else:
            return None

    def update_task_assignments_current_by_task_id(self, taskid, current):
        update_sql = f"update task_assignments set current = '{current}' where task_id = '{taskid}';"
        result = self.execute_insert_sql_no_wait(update_sql)
        return result

    def get_worker_report_info_by_hitid(self, hitid):
        select_sql = f"select hit_timespent, is_qa from work_reports where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result
        else:
            return None

    def get_contact_info_by_contact_id_vm(self, contact_id):
        select_sql = f"select environment, background, oneforma_id, call_type, mobile_type, system_phone_number, customer_phone_number, disconnect_timestamp, contact_duration, country, voip, audio_length from contact_info where contact_id = '{contact_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None


    def get_contact_ids_from_engserver(self):
        select_sql = "select contact_id from contact_info;"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def get_contact_ids_from_engserver_view(self):
        select_sql = "select contact_id from contact_view;"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def get_contact_ids_from_engserver_view_not_finished(self):
        select_sql = "select contact_id from contact_view where qa_result = 'Not Finished';"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def get_contact_ids_from_engserver_get_attr(self):
        select_sql = "select contact_id from contact_info where is_attr_get = 0;"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def get_contact_ids_from_engserver_get_search(self, call_center):
        select_sql = f"select contact_id from contact_info where is_search_get = 0 and call_center = '{call_center}';"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def save_new_contact_id_to_engserver(self, contact_id):
        insert_sql = f"insert into contact_info (contact_id) values('{contact_id}');"
        return self.execute_insert_sql_no_wait(insert_sql)

    def save_contact_view_to_engserver(self, contact_id, hitid, taskid, fixed_oneforma_id, qa_result, contact_info_id):
        insert_sql = f"replace into contact_view (contact_id,hitid,taskid,fixed_oneforma_id,qa_result,contact_info_id) values('{contact_id}','{hitid}','{taskid}','{fixed_oneforma_id}','{qa_result}','{contact_info_id}');"
        return self.execute_insert_sql_no_wait(insert_sql)

    def save_audiopath_audiolength_speechlength_to_engserver(self, contact_id, audio_path, audio_length, speech_length,
                                                             is_calculated):
        audio_path = self.escape_string(audio_path)
        insert_sql = f"update contact_info set audio_path = '{audio_path}', audio_length = '{audio_length}', speech_length = '{speech_length}', is_calculated = {is_calculated} where contact_id = '{contact_id}';"
        return self.execute_insert_sql_no_wait(insert_sql)

    def save_contact_ids_attr_to_engserver(self, contact_attr_dict):
        for key, value in contact_attr_dict.items():
            attr_environment = value[
                'environment'] if "environment" in value else ""
            attr_background = value[
                'background'] if "background" in value else ""
            attr_greetingPlayed = value[
                'greetingPlayed'] if "greetingPlayed" in value else ""
            attr_oneforma_id = value[
                'oneforma_id'] if "oneforma_id" in value else ""
            attr_call_type = value['call_type'] if "call_type" in value else ""
            attr_mobile_type = value[
                'mobile_type'] if "mobile_type" in value else ""
            attr_voip = value['voip'] if "voip" in value else ""
            insert_sql = f'''replace into contact_info (
                contact_id, 
                environment, 
                background,
                greetingplayed,
                oneforma_id,
                call_type,
                mobile_type,
                voip,
                is_attr_get
                ) values (
                    '{key}',
                    '{attr_environment}',
                    '{attr_background}',
                    '{attr_greetingPlayed}',
                    '{attr_oneforma_id}',
                    '{attr_call_type}',
                    '{attr_mobile_type}',
                    '{attr_voip}',
                    1
                )
            '''
            result = self.execute_insert_sql_no_wait(insert_sql)
            if result:
                return True
            else:
                return False

    def save_contact_id_attr_to_engserver(self, contact_id, contact_attr_dict,
                                          call_center):
        attr_environment = contact_attr_dict[
            'environment'] if "environment" in contact_attr_dict else ""
        attr_background = contact_attr_dict[
            'background'] if "background" in contact_attr_dict else ""
        attr_greetingPlayed = contact_attr_dict[
            'greetingPlayed'] if "greetingPlayed" in contact_attr_dict else ""
        attr_oneforma_id = contact_attr_dict[
            'oneforma_id'] if "oneforma_id" in contact_attr_dict else ""
        attr_call_type = contact_attr_dict[
            'call_type'] if "call_type" in contact_attr_dict else ""
        attr_mobile_type = contact_attr_dict[
            'mobile_type'] if "mobile_type" in contact_attr_dict else ""
        attr_voip = contact_attr_dict[
            'voip'] if "voip" in contact_attr_dict else ""
        insert_sql = f'''replace into contact_info (contact_id, environment, background,greetingplayed,oneforma_id,call_type,mobile_type, voip,is_attr_get,call_center) values (
                '{contact_id}',
                '{attr_environment}',
                '{attr_background}',
                '{attr_greetingPlayed}',
                '{attr_oneforma_id}',
                '{attr_call_type}',
                '{attr_mobile_type}',
                '{attr_voip}',
                1,
                '{call_center}'
            );
        '''
        return self.execute_insert_sql_no_wait(insert_sql)

    def save_contact_search_result_to_engserver(self, search_result_dict):
        if "Contact ID" not in search_result_dict.keys():
            return False
        else:
            contact_id = search_result_dict["Contact ID"]
            attr_system_number = search_result_dict[
                'System phone number'].strip(
                '+') if "System phone number" in search_result_dict else ""
            attr_customer_number = search_result_dict[
                'Customer phone number'].strip(
                '+'
            ) if "Customer phone number" in search_result_dict else ""
            attr_disconnect_timestamp = search_result_dict[
                'Disconnect timestamp'] if "Disconnect timestamp" in search_result_dict else ""
            attr_contact_duration = search_result_dict[
                'Contact duration'].strip(
                '\n') if "Contact duration" in search_result_dict else ""
            attr_country = config.ring_qa_system_phone_dict.get(attr_system_number)
            if attr_country is None:
                attr_country = 'Default'
            if attr_country == 'VMEN':
                if attr_customer_number[:1] != '1':
                    attr_country = 'VMSP'

            update_sql = f'''update contact_info set
                system_phone_number = '{attr_system_number}',
                customer_phone_number = '{attr_customer_number}',
                disconnect_timestamp = '{attr_disconnect_timestamp}',
                contact_duration = '{attr_contact_duration}',
                country = '{attr_country}',
                is_search_get = 1
                where contact_id = '{contact_id}';
            '''
            return self.execute_insert_sql_no_wait(update_sql)

    def update_is_upload(self, contact_id, blob_path=""):
        if blob_path == "":
            update_sql = f"update contact_info set is_upload = 1 where contact_id = '{contact_id}';"
        else:
            update_sql = f"update contact_info set is_upload = 1, blob_path = '{blob_path}' where contact_id = '{contact_id}';"
        return self.execute_insert_sql_no_wait(update_sql)

    def update_is_upload_copylocal(self, contact_id):
        update_sql = f"update contact_info set is_upload = 2 where contact_id = '{contact_id}';"
        return self.execute_insert_sql_no_wait(update_sql)

    def get_contact_id_not_uploaded(self):
        select_sql = f"SELECT contact_id FROM contact_info where is_upload = 0 and is_attr_get = 1 and is_search_get =1 and is_calculated = 1;"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def get_contact_id_not_calculated(self):
        select_sql = f"SELECT contact_id FROM contact_info where is_calculated = 0;"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def get_contact_id_not_calculated_history(self):
        select_sql = f"SELECT contact_id FROM contact_info where audio_length = 0;"
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
        return contact_ids

    def get_contact_info_not_uploaded(self):
        try:
            content_dict_list = []
            select_sql = f'''SELECT contact_id, environment, background, greetingplayed, oneforma_id, call_type, mobile_type, voip, system_phone_number, customer_phone_number, disconnect_timestamp, contact_duration, country, call_center, audio_length, speech_length FROM contact_info where is_upload = 0 and is_attr_get = 1 and is_search_get =1 and is_calculated = 1;
            '''
            result = self.execute_select_sql(select_sql)
            if len(result) > 0:
                for attr_result in result:
                    if attr_result != None:
                        attr_contact_id = attr_result[0]
                        attr_environment = attr_result[1]
                        attr_background = attr_result[2]
                        attr_greetingPlayed = attr_result[3]
                        attr_oneforma_id = attr_result[4]
                        attr_call_type = attr_result[5]
                        attr_mobile_type = attr_result[6]
                        attr_voip = attr_result[7]
                        attr_system_phone_number = attr_result[8]
                        attr_customer_phone_number = attr_result[9]
                        attr_disconnect_timestamp = attr_result[10]
                        attr_contact_duration = attr_result[11]
                        attr_country = attr_result[12]
                        attr_call_center = attr_result[13]
                        attr_audio_length = attr_result[14]
                        attr_speech_length = attr_result[15]

                        attr_dict = {
                            "contact_id": attr_contact_id,
                            "contact_info": {
                                "contactid": attr_contact_id,
                                "environment": attr_environment,
                                "background": attr_background,
                                "greetingplayed": attr_greetingPlayed,
                                "oneforma_id": attr_oneforma_id,
                                "call_type": attr_call_type,
                                "mobile_type": attr_mobile_type,
                                "voip": attr_voip,
                                "date": attr_disconnect_timestamp,
                                "telephone_number": attr_customer_phone_number,
                                "System_phone_number":
                                    attr_system_phone_number,
                                "Contact_duration": attr_contact_duration[1:],
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

    def get_audio_path_by_contact_id(self, contact_id):
        try:
            select_sql = f"SELECT audio_path FROM contact_info where contact_id = '{contact_id}';"
            result = self.execute_select_sql(select_sql)
            if len(result) > 0:
                return result[0][0]
            return None
        except Exception as e:
            print(e)
            raise

    def get_audio_length_by_contact_id(self, contact_id):
        try:
            select_sql = f"SELECT audio_length FROM contact_info where contact_id = '{contact_id}';"
            result = self.execute_select_sql(select_sql)
            if len(result) > 0:
                return result[0][0]
            return None
        except Exception as e:
            print(e)
            raise

    def get_country_by_contact_id(self, contact_id):
        try:
            select_sql = f"SELECT country FROM contact_info where contact_id = '{contact_id}';"
            result = self.execute_select_sql(select_sql)
            if len(result) > 0:
                return result[0][0]
            return None
        except Exception as e:
            print(e)
            raise

    def get_id_by_contact_id(self, contact_id):
        try:
            select_sql = f"SELECT id FROM contact_info where contact_id = '{contact_id}';"
            result = self.execute_select_sql(select_sql)
            if len(result) > 0:
                return result[0][0]
            return None
        except Exception as e:
            print(e)
            raise

    def get_oneforma_id_by_contact_id(self, contact_id):
        try:
            select_sql = f"SELECT oneforma_id FROM contact_info where contact_id = '{contact_id}';"
            result = self.execute_select_sql(select_sql)
            if len(result) > 0:
                return result[0][0]
            return None
        except Exception as e:
            print(e)
            raise