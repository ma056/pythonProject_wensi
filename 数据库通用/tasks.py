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

    def create_task(self, task_name: str, webapp_id: int) -> int:
        task_name = self.escape_string(task_name)
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            insert_sql = f"insert into tasks (webappid, taskname, uploader, internal_taskname, upload_date, priority) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2);"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    def create_task_taskgroup_id(self, task_name: str, webapp_id: int, taskgroup_id: int) -> int:
        task_name = self.escape_string(task_name)
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            insert_sql = f"insert into tasks (webappid, taskname, taskgroup_id, uploader, internal_taskname, upload_date, priority) values ({webapp_id},'{task_name}',{taskgroup_id},'{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2);"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    def create_task_all_limited(self, task_name: str, webapp_id: int) -> int:
        task_name = self.escape_string(task_name)
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            insert_sql = f"insert into tasks (webappid, taskname, uploader, internal_taskname, upload_date, priority, limited, qa_limited) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2,1,1);"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    def create_task_multi(self,
                          task_name: str,
                          webapp_id: int,
                          multi: int = 3) -> int:
        task_name = self.escape_string(task_name)
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            insert_sql = f"insert into tasks (webappid, taskname, uploader, internal_taskname, upload_date, priority, jperhit) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2, {multi});"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    def create_task_multi_limited(self,
                                  task_name: str,
                                  webapp_id: int,
                                  multi: int = 3) -> int:
        task_name = self.escape_string(task_name)
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            insert_sql = f"insert into tasks (webappid, taskname, uploader, internal_taskname, upload_date, priority, jperhit, limited, qa_limited) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2, {multi},1,1);"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    def create_task_FC(self, task_name: str, webapp_id: int) -> int:
        task_name = self.escape_string(task_name)
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            insert_sql = f"insert into tasks (webappid, taskname, uploader, internal_taskname, upload_date, priority) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2);"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
                return result[0][0]
            else:
                return None
        else:
            return -1

    def create_task_limited(self, task_name: str, webapp_id: int) -> int:
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        task_name = self.escape_string(task_name)
        hlmd5 = hashlib.md5()
        hlmd5.update(task_name.encode("utf-8"))
        internal_taskname = hlmd5.hexdigest()
        if result == None or len(result) == 0:
            insert_sql = f"insert into tasks (webappid, taskname, uploader, internal_taskname, upload_date, priority, limited) values ({webapp_id},'{task_name}','{self.uploader}','{internal_taskname}','{now().strftime('%Y-%m-%d %H:%M:%S')}',2,1);"
            is_exists = self.execute_insert_sql(insert_sql)
            if is_exists:
                select_sql = f"select taskid from tasks where taskname = '{task_name}';"
                result = self.execute_select_sql(select_sql)
            else:
                return None
        return result[0][0]

    def get_task_id_by_name(self, task_name: str) -> int:
        select_sql = f"select taskid from tasks where taskname = '{task_name}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_task_id_by_name_webapp_id(self, task_name: str,
                                      webapp_id: int) -> int:
        select_sql = f"select taskid from tasks where taskname = '{task_name}' and webappid = '{webapp_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]



    def get_task_name_by_id(self, task_id: int) -> str:
        select_sql = f"select taskname from tasks where taskid = '{task_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_aws_service_by_task_id(self, task_id: int):
        select_sql = f"select aws_service from tasks where taskid = '{task_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_webapp_id_by_task_id(self, task_id: int) -> str:
        select_sql = f"select webappid from tasks where taskid = '{task_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_task_status_by_id(self, task_id: int) -> int:
        select_sql = f"select status from tasks where taskid = '{task_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_task_internal_taskname_by_id(self, task_id: int) -> str:
        select_sql = f"select internal_taskname from tasks where taskid = '{task_id}';"
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]



    def get_task_ids_by_webapp_id(self, webapp_id):
        select_sql = f"select taskid from tasks where webappid = '{webapp_id}';"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_task_ids_by_webapp_id_and_status4(self, webapp_id):
        select_sql = f"select taskid from tasks where status =4 and webappid = '{webapp_id}';"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_task_ids_by_webapp_id_and_status4_and_batch(self, webapp_id, batch):
        select_sql = f"select taskid from tasks where status =4 and webappid = '{webapp_id}' and taskgroup_id = '{batch}';"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_task_ids_by_webapp_id_and_and_batch(self, webapp_id, batch):
        select_sql = f"select taskid from tasks where webappid = '{webapp_id}' and taskgroup_id = '{batch}';"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_task_ids_tasknames_by_webapp_id(self, webapp_id):
        select_sql = f"select taskid, taskname from tasks where webappid = '{webapp_id}';"
        result = self.execute_select_sql(select_sql)
        ret_list = []
        if len(result) > 0:
            for i in range(0, len(result)):
                if result[i] != None:
                    ret_list.append(result[i])
        return ret_list

    def get_task_ids_tasknames_by_webapp_id_inner_taskname(self, webapp_id, inner_taskname):
        select_sql = f"select taskid, taskname from tasks where webappid = '{webapp_id}' and taskname like '%{inner_taskname}%';"
        result = self.execute_select_sql(select_sql)
        ret_list = []
        if len(result) > 0:
            for i in range(0, len(result)):
                if result[i] != None:
                    ret_list.append(result[i])
        return ret_list

    def get_all_producting_task_by_webappid(self, webappid):
        select_sql = f"select taskid, limited from tasks where webappid = {webappid} and aws_service = 0;"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result
        else:
            return None

    def get_current_producting_task_by_webappid(self, webappid):
        select_sql = f"select taskid from tasks where webappid = {webappid} and aws_service = 0 and limited is null;"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return []

    def get_all_qaing_task_by_webappid(self, webappid):
        select_sql = f"select taskid, qa_limited from tasks where webappid = {webappid} and aws_service = 1 and s3_bucket = 0;"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result
        else:
            return None

    def get_current_qaing_task_by_webappid(self, webappid):
        select_sql = f"select taskid from tasks where webappid = {webappid} and aws_service = 1 and s3_bucket = 0 and qa_limited is null;"
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return []

    def get_all_qa_done_task_by_webappid_gracetitles(self, webappid):
        select_sql = f"select taskid from tasks where webappid = {webappid} and aws_service = 1 and s3_bucket = 1;"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result
        else:
            return None

    def update_taskname_by_task_id(self, task_id, task_name):
        update_sql = f"update tasks set taskname = '{task_name}' where taskid = {task_id};"
        self.execute_insert_sql(update_sql)
        return True

    def update_taskgroup_by_taskid(self, taskgroup_id, taskid):
        update_sql = f"update tasks set taskgroup_id = {taskgroup_id} where taskid = {taskid};"
        print(update_sql)
        return self.execute_insert_sql_no_wait_ret_id(update_sql)

    def update_limited_by_taskid(self, limited, taskid):
        if taskid is None:
            return
        if limited is None:
            update_sql = f"update tasks set limited = null where taskid = {taskid};"
        else:
            update_sql = f"update tasks set limited = {limited} where taskid = {taskid};"

        self.execute_insert_sql_no_wait(update_sql)

    def update_qa_limited_by_taskid(self, qa_limited, taskid):
        if taskid is None:
            return
        if qa_limited is None:
            update_sql = f"update tasks set qa_limited = null where taskid = {taskid};"
        else:
            update_sql = f"update tasks set qa_limited = {qa_limited} where taskid = {taskid};"

        self.execute_insert_sql_no_wait(update_sql)

    def update_s3_bucket_by_taskid(self, s3_bucket, taskid):
        if taskid is None:
            return
        update_sql = f"update tasks set s3_bucket = {s3_bucket} where taskid = {taskid};"
        self.execute_insert_sql_no_wait(update_sql)

    def update_aws_service_by_taskid(self, aws_service, taskid):
        if taskid is None:
            return
        update_sql = f"update tasks set aws_service = {aws_service} where taskid = {taskid};"
        self.execute_insert_sql_no_wait(update_sql)