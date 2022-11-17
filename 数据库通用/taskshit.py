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

    ## for Ring QA
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

    def create_audio_hit_limited(self, task_name: str, given_data: str,
                                 file_url: str, blob_path: str, webapp_id):
        task_id = self.create_task_limited(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '', '{blob_path}');"
        self.execute_insert_sql(insert_sql)

    ## for Ring QA
    def create_audio_hits(self, content_dict_list: list, webapp_id=0):
        for content_dict in content_dict_list:
            if "task_name" not in content_dict.keys(
            ) or "given_data" not in content_dict.keys(
            ) or "blob_path" not in content_dict.keys(
            ) or "file_url" not in content_dict.keys():
                print("missing key")
                return False
        tmp_task_id = 0
        dict_length = len(content_dict_list)
        for i in range(0, dict_length):

            task_name = content_dict_list[i]["task_name"]
            if i > 0 and task_name == content_dict_list[i - 1]["task_name"]:
                task_id = tmp_task_id
            else:
                task_id = self.create_task(task_name, webapp_id)
                tmp_task_id = task_id
            given_data = self.escape_string(content_dict_list[i]['given_data'])
            file_url = content_dict_list[i]['file_url']
            blob_path = content_dict_list[i]["blob_path"]
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '', '{blob_path}');"
            self.execute_insert_sql(insert_sql)
            print(f"{task_name} --- {file_url} --- Done")
        return True

    def create_audio_hit(self,
                         task_name: str,
                         given_data: str,
                         blob_path: str,
                         file_url: str,
                         webapp_id=0):
        task_name = self.escape_string(task_name)
        task_id = self.create_task(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}');"
        self.execute_insert_sql(insert_sql)
        return True



    ## for Form Collection
    def create_txt_hits_FC(self, task_name, given_data: str, webapp_id=0):
        task_id = self.create_task_FC(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        if task_id == -1:
            print(f"{task_name} exists")
            return
        given_data = self.escape_string(given_data)
        task_name = self.escape_string(task_name)
        select_sql = f"select hitid from tasks_hits where taskid = {task_id};"
        result = self.execute_select_sql(select_sql)
        hit_count = len(result)
        if hit_count >= 0:
            for i in range(hit_count, 80):
                insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename) values ({task_id},'{given_data}', 1, '{task_name}', '');"
                self.execute_insert_sql(insert_sql)
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done", end="\r")

    def create_txt_hits_FC_limited(self,
                                   task_name,
                                   given_data: str,
                                   webapp_id=0):
        task_id = self.create_task_limited(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        print(f"====Create hits for {task_id}:{task_name}====")
        for i in range(0, 50):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename) values ({task_id},'{given_data}', 1, '{task_name}', '');"
            self.execute_insert_sql_no_wait(insert_sql)
            print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits(self,
                        task_name,
                        given_data: str,
                        webapp_id,
                        hits_limit=1,
                        fileurl=''):
        task_id = self.create_task(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename) values ({task_id},'{given_data}', 1, '{fileurl}', '');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_limited(self,
                                task_name,
                                given_data: str,
                                webapp_id,
                                hits_limit=1,
                                fileurl=''):
        task_id = self.create_task_limited(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename) values ({task_id},'{given_data}', 1, '{fileurl}', '');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_limited_autofill(self,
                                         task_name,
                                         given_data: str,
                                         webapp_id,
                                         datahandled,
                                         hits_limit=1,
                                         fileurl='',
                                         done_by="Automatic",
                                         submit_time=strnow()):
        task_id = self.create_task_limited(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        datahandled = self.escape_string(datahandled)
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, data_handled, done_by, submit_time) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{datahandled}', '{done_by}', '{submit_time}');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_mhitid(self,
                               task_name,
                               given_data: str,
                               webapp_id,
                               mhitid,
                               hits_limit=1,
                               fileurl=''):
        task_id = self.create_task(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mhitid) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_mhitid_limited(self,
                                       task_name,
                                       given_data: str,
                                       webapp_id,
                                       mhitid,
                                       hits_limit=1,
                                       fileurl=''):
        task_id = self.create_task_limited(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mhitid) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_berkus(self,
                               task_name,
                               given_data: str,
                               webapp_id,
                               internal_id,
                               hits_limit=1,
                               fileurl=''):
        task_id = self.create_task_limited(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, hitInternalName) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{internal_id}');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_multi(self,
                              task_name,
                              given_data: str,
                              webapp_id,
                              multi=3,
                              fileurl=''):
        task_id = self.create_task_multi(task_name, webapp_id, multi)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql(insert_sql)
            if multi != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_multi_limited_autofill(self,
                                               task_name,
                                               given_data: str,
                                               webapp_id,
                                               datahandled,
                                               multi=3,
                                               fileurl='',
                                               done_by="Automatic",
                                               submit_time=strnow()):
        task_id = self.create_task_multi_limited(task_name, webapp_id, multi)
        datahandled = self.escape_string(datahandled)
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID, data_handled, done_by, submit_time) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}', '{datahandled}', '{done_by}', '{submit_time}');"
            self.execute_insert_sql(insert_sql)
            if multi != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_multi_limited(self,
                                      task_name,
                                      given_data: str,
                                      webapp_id,
                                      multi=3,
                                      fileurl=''):
        task_id = self.create_task_multi_limited(task_name, webapp_id, multi)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql(insert_sql)
            if multi != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_multi_different_givendata(self,
                                                  task_name,
                                                  given_data: list,
                                                  webapp_id,
                                                  multi=3,
                                                  fileurl=''):
        if len(given_data) != multi:
            raise Exception("given_data length not equal to multi")
        task_id = self.create_task_multi(task_name, webapp_id, multi)
        # print(f"====Create hits for {task_id}:{task_name}====")
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID) values ({task_id},'{self.escape_string(given_data[i])}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql_no_wait(insert_sql)
            if multi != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_edu_round2_hits_multi(self,
                                     task_name: str,
                                     webapp_id,
                                     fileurl,
                                     ruleset: str,
                                     given_data: str,
                                     data_handled,
                                     done_by,
                                     submit_time,
                                     blob_path,
                                     internal=5,
                                     multi=3
                                     ):
        task_id = self.create_task_multi_limited(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        data_handled = self.escape_string(data_handled)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID, ruleset, data_handled, done_by, submit_time, blob_path) values ({task_id},'{given_data}', {internal}, '{fileurl}', '', '{mhitid}', '{ruleset}', '{data_handled}', '{done_by}', '{submit_time}', '{blob_path}');"
        self.execute_insert_sql(insert_sql)
        print(f"{task_name} --- Create multi hit 1/3 {mhitid} --- Done")
        for i in range(0, multi - 1):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID, blob_path) values ({task_id},'{given_data}', {internal}, '{fileurl}', '', '{mhitid}', '{blob_path}');"
            self.execute_insert_sql(insert_sql)
            if multi != 1:
                print(f"{task_name} --- Create multi hit {str(i + 2)}/3 {mhitid} --- Done")

    def create_txt_hits_multi_ruleset(self,
                                      task_name,
                                      given_data: str,
                                      webapp_id,
                                      ruleset,
                                      multi=3,
                                      fileurl=''):
        task_id = self.create_task_multi(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID, ruleset) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}', '{ruleset}');"
            self.execute_insert_sql(insert_sql)
            if multi != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_multi_ruleset_hitinternalname(self,
                                                      task_name,
                                                      given_data: str,
                                                      webapp_id,
                                                      ruleset,
                                                      hitinternalname,
                                                      multi=3,
                                                      fileurl=''):
        task_id = self.create_task_multi(task_name, webapp_id)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID, ruleset, hitInternalName) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}', '{ruleset}', '{hitinternalname}');"
            self.execute_insert_sql(insert_sql)

    def create_txt_hits_multi_ruleset_hitinternalname_limited(self,
                                                              task_name,
                                                              given_data: str,
                                                              webapp_id,
                                                              ruleset,
                                                              hitinternalname,
                                                              multi=3,
                                                              fileurl=''):
        task_id = self.create_task_multi_limited(task_name, webapp_id, multi)
        # print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        for i in range(0, multi):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID, ruleset, hitInternalName) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}', '{ruleset}', '{hitinternalname}');"
            self.execute_insert_sql(insert_sql)



    def create_txt_hits_words_count(self,
                                    task_name,
                                    given_data: str,
                                    webapp_id,
                                    hits_limit=1):
        task_id = self.create_task(task_name, webapp_id)
        print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename) values ({task_id},'{given_data}', 1, '{task_name}', '');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_txt_hits_by_id(self, task_id, given_data: str, hits_limit=1):
        task_name = self.get_task_name_by_id(task_id)
        print(f"====Create hits for {task_id}:{task_name}====")
        given_data = self.escape_string(given_data)
        for i in range(0, hits_limit):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename) values ({task_id},'{given_data}', 1, '{task_name}', '');"
            self.execute_insert_sql(insert_sql)
            if hits_limit != 1:
                print(f"{task_name} --- Create hit {str(i + 1)} times --- Done")

    def create_us_file_hit(self, task_name: str, given_data: str,
                           file_url: str, blob_path: str, webapp_id):
        task_id = self.create_task(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_us_file_hit_with_taskgroup_id(self, task_name: str, given_data: str,
                                             file_url: str, blob_path: str, webapp_id, taskgroup_id: int):
        task_id = self.create_task_taskgroup_id(task_name, webapp_id, taskgroup_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_us_file_hit_with_pro_data(self, task_name: str, given_data: str,
                                         file_url: str, blob_path: str, webapp_id, datahandled, done_by="Automatic",
                                         submit_time=strnow()):
        task_id = self.create_task(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        datahandled = self.escape_string(datahandled)
        file_url = self.escape_string(file_url)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path, data_handled, done_by, submit_time) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}', '{datahandled}', '{done_by}', '{submit_time}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_us_file_hit_limit(self, task_name: str, given_data: str,
                                 file_url: str, blob_path: str, webapp_id):
        task_id = self.create_task_limited(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_us_file_hit_limit_with_pro(self, task_name: str, given_data: str,
                                          file_url: str, blob_path: str, webapp_id, datahandled, done_by="Automatic",
                                          submit_time=strnow()):
        task_id = self.create_task_limited(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        datahandled = self.escape_string(datahandled)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path, data_handled, done_by, submit_time) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}', '{datahandled}','{done_by}','{submit_time}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_us_file_hit_limit_edu(self, task_name: str, given_data: str,
                                     file_url: str, blob_path: str, webapp_id, done_by, datahandled, submit_time):
        task_id = self.create_task_limited(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        if done_by is None or datahandled is None:
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}');"
        else:
            datahandled = self.escape_string(datahandled)
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path, data_handled, done_by, submit_time) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}', '{datahandled}', '{done_by}', '{submit_time}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_us_file_hit_internalhitname(self, task_name: str, given_data: str,
                                           file_url: str, blob_path: str, webapp_id, hitinternalname):
        task_id = self.create_task(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path, hitInternalName) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}', '{hitinternalname}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_us_file_hit_internalhitname_limited(self, task_name: str, given_data: str,
                                                   file_url: str, blob_path: str, webapp_id, hitinternalname):
        task_id = self.create_task_limited(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path, hitInternalName) values ({task_id},'{given_data}', 5, '{file_url}', '{internal_filename}', '{blob_path}', '{hitinternalname}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_fileshare_file_hit_hitinternalname(self, task_name: str, given_data: str,
                                                  file_url: str, webapp_id, hit_internal_name):
        task_id = self.create_task(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, hitInternalName) values ({task_id},'{given_data}', 1, '{file_url}', '{file_url}', '{hit_internal_name}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def create_hk_file_hit(self, task_name: str, given_data: str,
                           file_url: str, blob_path: str, webapp_id):
        task_id = self.create_task(task_name, webapp_id)
        given_data = self.escape_string(given_data)
        hlmd5 = hashlib.md5()
        hlmd5.update(file_url.encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, blob_path) values ({task_id},'{given_data}', 6, '{file_url}', '{internal_filename}', '{blob_path}');"
        self.execute_insert_sql(insert_sql)

    def update_given_data_by_hitid(self, given_data, hitid):
        given_data = self.escape_string(given_data)
        update_sql = f"update tasks_hits set given_data = '{given_data}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_datahandeld_qadata_by_hitid(self, datahandled, qa_data, hitid):
        date_time = strnow()
        update_sql = f"update tasks_hits set data_handled = '{datahandled}', qa_data = '{qa_data}', done_by = '{datahandled}', qa_reviewer = '{qa_data}', submit_time = '{date_time}', qa_submit_time = '{date_time}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_datahandeld_doneby_submittime_qadata_qareviewer_qasubmittime_by_hitid(self, datahandled, done_by,
                                                                                     submit_time, qa_data, qa_reviewer,
                                                                                     qa_submittime, hitid):
        if qa_data is not None:
            qa_data = self.escape_string(qa_data)
            update_sql = f"update tasks_hits set data_handled = '{datahandled}', done_by = '{done_by}', submit_time = '{submit_time}', qa_data = '{qa_data}',  qa_reviewer = '{qa_reviewer}',  qa_submit_time = '{qa_submittime}' where HitID = {hitid};"
        else:
            datahandled = self.escape_string(datahandled)
            update_sql = f"update tasks_hits set data_handled = '{datahandled}', done_by = '{done_by}', submit_time = '{submit_time}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_datahandeld_doneby_submittime_by_hitid(self, datahandled, done_by, submit_time, hitid):
        datahandled = self.escape_string(datahandled)
        update_sql = f"update tasks_hits set data_handled = '{datahandled}', done_by = '{done_by}', submit_time = '{submit_time}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_datahandeld_by_hitid(self, datahandled, hitid):
        datahandled = self.escape_string(datahandled)
        update_sql = f"update tasks_hits set data_handled = '{datahandled}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)


    def update_givendata_by_hitid(self, datahandled, hitid):
        datahandled = self.escape_string(datahandled)
        update_sql = f"update tasks_hits set given_data = '{datahandled}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_qadata_by_hitid(self, datahandled, hitid):
        datahandled = self.escape_string(datahandled)
        update_sql = f"update tasks_hits set qa_data = '{datahandled}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_datahandeld_doneby_submittime_ruleset_by_hitid(self, datahandled, done_by, submit_time, ruleset, hitid):
        datahandled = self.escape_string(datahandled)
        update_sql = f"update tasks_hits set data_handled = '{datahandled}', done_by = '{done_by}', submit_time = '{submit_time}', ruleset = '{ruleset}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_qadata_qareviewer_qasubmittime_by_hitid(self, qa_data, qa_reviewer, qa_submittime, hitid):
        if qa_data == 'null':
            update_sql = f"update tasks_hits set qa_data = {qa_data},  qa_reviewer = {qa_reviewer},  qa_submit_time = {qa_submittime} where HitID = {hitid};"
        else:
            qa_data = self.escape_string(qa_data)
            update_sql = f"update tasks_hits set qa_data = '{qa_data}',  qa_reviewer = '{qa_reviewer}',  qa_submit_time = '{qa_submittime}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_qadata_qareviewer_qasubmittime_engineeringmc_by_hitid(self, qa_data, qa_reviewer, qa_submittime,
                                                                     engineeringmc, hitid):
        qa_data = self.escape_string(qa_data)
        update_sql = f"update tasks_hits set qa_data = '{qa_data}',  qa_reviewer = '{qa_reviewer}',  qa_submit_time = '{qa_submittime}', engineeringmc_file = '{engineeringmc}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def revert_qa_by_hitid(self, hitid):
        update_sql = f"update tasks_hits set qa_data = null,  qa_reviewer = null,  qa_submit_time = null, start_handling_time = null where HitID = {hitid};"
        return self.execute_insert_sql_no_wait(update_sql)

    def revert_pro_by_hitid(self, hitid):
        update_sql = f"update tasks_hits set data_handled = null,  done_by = null,  submit_time = null, start_handling_time = null where HitID = {hitid};"
        return self.execute_insert_sql_no_wait(update_sql)

    def update_doneby_qareviewer_by_hitid(self, done_by, qa_reviewer, hitid):
        update_sql = f"update tasks_hits set done_by = '{done_by}', qa_reviewer = '{qa_reviewer}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_doneby_by_hitid(self, done_by, hitid):
        update_sql = f"update tasks_hits set done_by = '{done_by}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_qareviewer_by_hitid(self, qa_reviewer, hitid):
        update_sql = f"update tasks_hits set qa_reviewer = '{qa_reviewer}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)





    def update_fileurl_by_hitid(self, fileurl, hitid):
        update_sql = f"update tasks_hits set fileurl = '{fileurl}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_engineermc_by_hitid(self, engieermc, hitid):
        update_sql = f"update tasks_hits set engineeringmc_file = '{engieermc}' where HitID = {hitid};"
        self.execute_insert_sql_no_wait(update_sql)



    def get_task_pro_start_time_by_id(self, task_id: int) -> str:
        select_sql = f"select submit_time from tasks_hits where taskid = '{task_id}' order by submit_time limit 0,1;"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_task_pro_end_time_by_id(self, task_id: int) -> str:
        select_sql = f"select submit_time from tasks_hits where taskid = '{task_id}' order by submit_time desc limit 0,1;"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_task_qa_start_time_by_id(self, task_id: int) -> str:
        select_sql = f"select qa_submit_time from tasks_hits where taskid = '{task_id}' order by qa_submit_time limit 0,1;"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_task_hit_count_by_task_id(self, task_id: int):
        select_sql = f"select count(*) from tasks_hits where taskid = '{task_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return 0
        else:
            return result[0][0]

    def get_task_pro_not_finish_count_by_task_id(self, task_id: int):
        select_sql = f"select count(*) from tasks_hits where taskid = '{task_id}' and done_by is null;"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return 0
        else:
            return result[0][0]

    def get_task_qa_not_finish_count_by_task_id(self, task_id: int):
        select_sql = f"select count(*) from tasks_hits where taskid = '{task_id}' and qa_reviewer is null;"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return 0
        else:
            return result[0][0]

    def get_task_qa_end_time_by_id(self, task_id: int) -> str:
        select_sql = f"select qa_submit_time from tasks_hits where taskid = '{task_id}' order by qa_submit_time desc limit 0,1;"
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


    def get_hits_info_by_task_id_telugu(self, task_id):
        select_sql = f"select hitid, fileurl, data_handled, qa_data, blob_path from tasks_hits where taskid = '{task_id}' order by hitid;"
        return self.execute_select_sql(select_sql)

    def get_hits_given_data_by_task_id(self, task_id):
        select_sql = f"select hitid, given_data from tasks_hits where taskid = '{task_id}' order by hitid;"
        return self.execute_select_sql(select_sql)

    def get_fileurl_count_group_by_task_id(self, task_id):
        select_sql = f"select fileurl,count(fileurl) from tasks_hits where taskid = '{task_id}' GROUP BY fileurl;"
        return self.execute_select_sql(select_sql)

    def get_hits_given_data_by_hit_id(self, hit_id):
        select_sql = f"select given_data from tasks_hits where hitid = '{hit_id}';"
        return self.execute_select_sql(select_sql)

    def get_given_data_by_hit_id(self, hit_id):
        select_sql = f"select given_data from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_hitInternalName_by_hit_id(self, hit_id):
        select_sql = f"select hitInternalName from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_fileurl_by_hit_id(self, hit_id):
        select_sql = f"select fileurl from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_task_id_by_hit_id(self, hit_id):
        select_sql = f"select taskID from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_fileurl_internalfilename_by_hit_id(self, hit_id):
        select_sql = f"select fileurl, internal_filename from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        return None

    def get_hits_data_handled_by_task_id(self, task_id):
        select_sql = f"select data_handled from tasks_hits where taskid = '{task_id}' order by hitid;"
        return self.execute_select_sql(select_sql)

    def get_hits_data_handled_by_hit_id(self, hit_id):
        select_sql = f"select data_handled from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_hits_data_handled_done_by_by_hit_id(self, hit_id):
        select_sql = f"select data_handled, done_by from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        return None

    def get_hits_taskid_datahandled_qadata_by_hit_id(self, hit_id):
        select_sql = f"select taskid, data_handled, qa_data from tasks_hits where hitid = '{hit_id}';"
        return self.execute_select_sql(select_sql)

    def get_done_by_by_hit_id(self, hit_id):
        select_sql = f"select done_by from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None

    def get_submittime_by_hit_id(self, hit_id):
        select_sql = f"select submit_time from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        return None



    def get_done_by_qa_data_qa_reviewer_by_hit_id(self, hit_id):
        select_sql = f"select done_by, qa_data, qa_reviewer from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        return None

    def get_done_by_qa_data_qa_reviewer_submittime_by_hit_id(self, hit_id):
        select_sql = f"select done_by, qa_data, qa_reviewer, submit_time, qa_submit_time from tasks_hits where hitid = '{hit_id}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        return None

    def get_hits_id_data_handled_by_task_id(self, task_id):
        select_sql = f"select hitid, data_handled from tasks_hits where taskid = '{task_id}' order by hitid;"
        return self.execute_select_sql(select_sql)

    def get_hits_id_by_task_id(self, task_id):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id};"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_pro_done_hitids_by_taskid_and_date(self, task_id, date_start, date_end):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id} and submit_time >= '{date_start}' and submit_time <= '{date_end}' and done_by is not null;"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_qa_done_hitids_by_taskid_and_date(self, task_id, date_start, date_end):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id} and qa_submit_time >= '{date_start}' and qa_submit_time <= '{date_end}' and qa_reviewer is not null;"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_hits_not_pro_id_by_task_id(self, task_id):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id} and done_by = 'Not to Pro';"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_hits_not_qa_id_by_task_id(self, task_id):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id} and qa_reviewer = 'Not to QA';"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_hits_id_by_task_id_hitinternalname(self, task_id, hitinternalname):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id} and hitInternalName = '{hitinternalname}';"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if result is None:
            return None
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_production_done_engmc_hits_id_by_task_id(self, task_id):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id} and done_by is not null and engineeringmc_file is null;"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_hits_id_by_task_id_done(self, task_id):
        select_sql = f"select hitid from tasks_hits where taskid = {task_id} and done_by is not null;"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return []

    def get_hit_id_by_task_id_fileurl(self, task_id, fileurl):
        select_sql = f"select hitid from tasks_hits where taskid = '{task_id}' and fileurl = '{fileurl}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_hit_id_by_task_ids_fileurl(self, task_ids, fileurl):
        select_sql = f"select hitid from tasks_hits where taskid in ({task_ids}) and fileurl = '{fileurl}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None


    def get_qadata_datahandle_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_by_hitid(self, hitid):
        select_sql = f"select qa_data from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def update_hit_taskid_by_hitid(self, hitid, taskid):
        select_sql = f"update tasks_hits set taskid = {taskid} where hitid = {hitid};"
        return self.execute_insert_sql(select_sql)

    def get_mHitID_by_hitid(self, hitid):
        select_sql = f"select mHitID from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_engineeringmc_file_by_hitid(self, hitid):
        select_sql = f"select engineeringmc_file from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_ruleset_by_hitid(self, hitid):
        select_sql = f"select ruleset from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_blob_path_by_hitid(self, hitid):
        select_sql = f"select blob_path from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_datahandeld_by_hitid(self, hitid):
        select_sql = f"select data_handled from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_qadata_datahandle_mhitid_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data, mHitID from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_fileurl_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data, fileurl from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_fileurl_blobpath_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data, fileurl,blob_path from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_givendata_datahandle_blobpath_by_hitid(self, hitid):
        select_sql = f"select given_data, data_handled, blob_path from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_givendata_datahandle_by_hitid(self, hitid):
        select_sql = f"select given_data, data_handled from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_fileurl_blobpath_by_hitid_engmc(self, hitid):
        select_sql = f"select data_handled, qa_data, fileurl,blob_path, engineeringmc_file from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_givendata_doneby_qareviewer_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data, given_data, done_by, qa_reviewer from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_mhitid_fileurl_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data, mHitID, fileurl from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_by_fileurl_taskid(self, fileurl, taskid):
        select_sql = f"select data_handled, qa_data from tasks_hits where fileurl = '{fileurl}' and taskid = {taskid} ;"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_doneby_submittime_qareviewer_qasubmittime_by_fileurl_taskid(self, fileurl, taskid):
        select_sql = f"select data_handled, qa_data, done_by, submit_time, qa_reviewer, qa_submit_time from tasks_hits where fileurl like '{fileurl}' and taskid = {taskid} ;"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_doneby_submittime_qareviewer_qasubmittime_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data, done_by, submit_time, qa_reviewer, qa_submit_time from tasks_hits where hitid = {hitid} ;"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_doneby_submittime_qareviewer_qasubmittime_ruleset_engineeringmc_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data, done_by, submit_time, qa_reviewer, qa_submit_time, ruleset, engineeringmc_file from tasks_hits where hitid = {hitid} ;"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_by_taskid_fileurl(self, taskid, fileurl):
        select_sql = f"select qa_data from tasks_hits where taskid = {taskid} and fileurl = '{fileurl}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_qadata_by_taskid_datahandled(self, taskid, datahandled):
        select_sql = f"select qa_data from tasks_hits where taskid = {taskid} and data_handled = '{datahandled}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_qadata_fileurl_by_hitid(self, hitid):
        select_sql = f"select qa_data, fileurl from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_final_data_by_hitid(self, hitid):
        select_sql = f"select data_handled, qa_data from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            datahandled = result[0][0]
            qadata = result[0][1]
            if qadata is not None:
                return qadata
            elif qadata is None and datahandled is not None:
                return datahandled
            else:
                return None
        else:
            return None

    def get_fileurl_by_hitid(self, hitid):
        select_sql = f"select fileurl from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_fileurl_givendata_by_hitid(self, hitid):
        select_sql = f"select fileurl, given_data from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_export_info_by_hitid(self, hitid):
        select_sql = f"select fileurl, given_data, ruleset, data_handled, hitinternalname, done_by, submit_time, qa_data from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None



    def get_qa_reviewer_by_hitid(self, hitid):
        select_sql = f"select qa_reviewer from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_qa_submittime_by_hitid(self, hitid):
        select_sql = f"select qa_submit_time from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0][0]
        else:
            return None

    def get_fileurl_datahandled_by_hitid(self, hitid):
        select_sql = f"select fileurl, data_handled from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def get_qadata_datahandle_by_hitid_ww(self, hitid):
        select_sql = f"select given_data, FileURL, data_handled, done_by, qa_data from tasks_hits where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None
