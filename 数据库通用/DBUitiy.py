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
    def __init__(self, usage: str, table_name: str):
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
        # self.table_name = table_name
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

    ## 针对tasks的操作
    # 返回create操作需要的数据
    def get_create_task_data(self, **kwargs):
        task_name = self.escape_string(kwargs['task_name'])
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        return task_name, result, internal_taskname, self.uploader

    # create 操作
    def create_task(self, **kwargs):
        if kwargs['result'] == None or len(kwargs['result']) == 0:
            insert_sql = kwargs['insert_sql']
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{kwargs['task_name']}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    # get操作主体分三种情况进行输出
    def get_task(self, **kwargs):
        select_sql = kwargs['select_sql']
        result = self.execute_select_sql(select_sql)
        if 'id_list' in kwargs:
            if len(result) > 0:
                for item in result:
                    kwargs['id_list'].append(item[0])
                return kwargs['id_list']
            else:
                return None
        elif 'ret_list' in kwargs:
            if len(result) > 0:
                for i in range(0, len(result)):
                    if result[i] != None:
                        kwargs['ret_list'].append(result[i])
            return kwargs['ret_list']
        else:
            if result == None or len(result) == 0:
                return None
            else:
                return result[0][0]

    # update操作
    def update_task(self, **kwargs):
        update_sql = kwargs['update_sql']
        return self.execute_insert_sql_no_wait(update_sql)

    ## tasks_hits操作
    # 获取create数据
    def get_create_tasks_hits_data(self, **kwargs):
        task_id = self.create_task(**kwargs)
        datahandled = self.escape_string(kwargs['datahandled'])
        given_data = self.escape_string(kwargs['given_data'])
        hlmd5 = hashlib.md5()
        hlmd5.update(kwargs['file_url'].encode("utf-8"))
        internal_filename = hlmd5.hexdigest()
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        return task_id, datahandled, given_data, mhitid, internal_filename

    # create操作
    def create_tasks_hits(self, **kwargs):
        if 'hit_limit' in kwargs:
            for i in range(0, kwargs['hits_limit']):
                insert_sql = kwargs['insert_sql']
                self.execute_insert_sql(insert_sql)
                if kwargs['hits_limit'] != 1:
                    print(f"{kwargs['task_name']} --- Create hit {str(i + 1)} times --- Done")
        else:
            insert_sql = kwargs['insert_sql']
            self.execute_insert_sql_no_wait(insert_sql)

    # get操作
    def get_tasks_hits(self, **kwargs):
        select_sql = kwargs['select_sql']
        result = self.execute_select_sql(select_sql)
        if 'id_list' in kwargs:
            if len(result) > 0:
                for item in result:
                    kwargs['id_list'].append(item[0])
                return kwargs['id_list']
            else:
                return []
        else:
            if result == None or len(result) == 0:
                return None
            elif len(result) > 0:
                return result[0][0]
            else:
                return None

    # update操作
    def update_tasks_hits(self, **kwargs):
        update_sql = kwargs['update_sql']
        self.execute_insert_sql_no_wait(update_sql)

    ## tasks和表tasks_hits 多表连接查询
    def get_tasks_taskshits(self, **kwargs):
        select_sql = kwargs['select_sql']
        result = self.execute_select_sql(select_sql)
        hit_id_list = []
        if result == None or len(result) == 0:
            return None
        elif len(result) > 0:
            for i in range(0, len(result)):
                if result[i] != None:
                    hit_id_list.append(result[i][0])
            return hit_id_list
        else:
            return result[0][0]

    ## 其他表
    # get操作通过某id进行查询
    def get_data_by_id(self, **kwargs):
        select_sql = kwargs['select_sql']
        result = self.execute_select_sql(select_sql)
        contact_ids = []
        if result == None or len(result) == 0:
            return None
        elif len(result) > 0:
            for item in result:
                if item != None:
                    contact_ids.append(item[0])
            return contact_ids, result
        else:
            return result[0][0]

    # replace into 操作
    def create_hit_metadata(self, **kwargs):
        insert_sql = kwargs['insert_sql']
        self.execute_insert_sql(insert_sql)

    # save操作
    def save_new_contact(self, **kwargs):
        insert_sql = kwargs['insert_sql']
        return self.execute_insert_sql_no_wait(insert_sql)

    # create操作
    def create_txt_hits(self, **kwargs):
        task_id = self.create_task(**kwargs)
        given_data = self.escape_string(kwargs['given_data'])
        temp_uuid = uuid.uuid4()
        mhitid = str(temp_uuid).split('-')[0] + str(temp_uuid).split('-')[1]
        fileurl = kwargs['fileurl']
        for i in range(0, kwargs['multi']):
            insert_sql = f"insert into tasks_hits (taskid, given_data, internal, FileURL, internal_filename, mHitID) values ({task_id},'{given_data}', 1, '{fileurl}', '', '{mhitid}');"
            self.execute_insert_sql(insert_sql)
            if kwargs['multi'] != 1:
                print(f"{kwargs['task_name']} --- Create hit {str(i + 1)} times --- Done")
        select_sql = f"select hitid from tasks_hits where FileURL = '{fileurl}' and taskid = {task_id};"
        result = self.execute_select_sql(select_sql)
        if len(result) == kwargs['multi']:
            for hitid in result:
                hitid = hitid[0]
                audio_length = kwargs['audio_length']
                replace_sql = f"replace into hit_metadata (HitID, metadata) values ({hitid},'{audio_length}');"
                self.execute_insert_sql(replace_sql)
        else:
            print(f"{fileurl} multi hit error")

# dbo = OneForma("Main")
# task_name, result, internal_taskname, uploader = dbo.get_create_task_data(**{"task_name": '_Transcription'})
# webapp_id = 1
# insert_sql = f"insert into tasks (webappid, taskname, uploader, internal_taskname, upload_date, priority) values ({webapp_id},'{task_name}','{uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2);"
# dbo.create_task(**{"task_name": '_Transcription', "insert_sql": insert_sql})
