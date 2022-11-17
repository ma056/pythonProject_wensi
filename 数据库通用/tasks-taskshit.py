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



    def get_qadata_by_taskId(self, task_id: int) -> int:
        select_sql = f'''
            select t1.HitID,t1.qa_data,t1.FileURL,t2.taskname from scribo_webapps_db.tasks_hits as t1
                join scribo_webapps_db.tasks as t2
            where t1.taskID = '{task_id}'
                and t1.taskID = t2.taskid
                and t1.qa_data not in ('REJECTED')
            '''
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result

    def get_datahandled_qadata_hitid_taskid_by_webappid_fileurl(self, fileurl: str,
                                                                webapp_id: int, exlcude_taskid: list = []) -> int:
        if len(exlcude_taskid) > 0:
            new_str = ""
            for taskid in exlcude_taskid:
                new_str += f"{taskid},"
            new_str = new_str[:-1]
            select_sql = f'''
            select data_handled, qa_data, hitid, t1.taskID from scribo_webapps_db.tasks_hits as t1
                join scribo_webapps_db.tasks as t2
            where t2.webappid = {webapp_id}
                and t1.taskID not in ({new_str})
                and t1.taskID = t2.taskid
                and t1.FileURL = '{fileurl}';
            '''
        else:
            select_sql = f'''
            select data_handled, qa_data, hitid, t1.taskID from scribo_webapps_db.tasks_hits as t1
                join scribo_webapps_db.tasks as t2
            where t2.webappid = {webapp_id}
                and t1.taskID = t2.taskid
                and t1.FileURL = '{fileurl}';
            '''
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0]

    def get_hitid_taskid_by_webappid_fileurl(self, fileurl: str,
                                             webapp_id: int, exlcude_taskid: list = []) -> int:
        if len(exlcude_taskid) > 0:
            new_str = ""
            for taskid in exlcude_taskid:
                new_str += f"{taskid},"
            new_str = new_str[:-1]
            select_sql = f'''
            select hitid, t1.taskID from scribo_webapps_db.tasks_hits as t1
                join scribo_webapps_db.tasks as t2
            where t2.webappid = {webapp_id}
                and t2.taskid not in ({new_str})
                and t1.taskID = t2.taskid
                and t1.FileURL = '{fileurl}';
            '''
        else:
            select_sql = f'''
            select hitid, t1.taskID from scribo_webapps_db.tasks_hits as t1
                join scribo_webapps_db.tasks as t2
            where t2.webappid = {webapp_id}
                and t1.taskID = t2.taskid
                and t1.FileURL = '{fileurl}';
            '''
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result

    def get_task_internal_taskname_by_hitid(self, hitid: int) -> str:
        select_sql = f'''
                        select t2.internal_taskname from scribo_webapps_db.tasks_hits as t1
                            join scribo_webapps_db.tasks as t2
                        where t1.hitid = {hitid}
                            and t1.taskID = t2.taskid;
        '''
        result = self.execute_select_sql(select_sql)
        if result == None or len(result) == 0:
            return None
        else:
            return result[0][0]

    def get_production_done_hit_ids_by_webapp_id_FC(self, webappid):
        select_sql = f'''
        select hitid from scribo_webapps_db.tasks_hits as t1
            join scribo_webapps_db.tasks as t2
        where t2.webappid = {webappid}
            and t2.upload_date > '2021-12-20 06:50:00'
            and t1.taskID = t2.taskid;
        '''
        # and t1.done_by is not null
        # and t1.done_by != 'skip';
        result = self.execute_select_sql(select_sql)
        hit_id_list = []
        if len(result) > 0:
            for i in range(0, len(result)):
                if result[i] != None:
                    hit_id_list.append(result[i][0])
        return hit_id_list


    def get_all_hit_ids_by_webapp_id(self, webapp_id):
        select_sql = f'''
        select hitid from scribo_webapps_db.tasks_hits as t1
            join scribo_webapps_db.tasks as t2
        where t2.webappid = {webapp_id}
            and t1.taskID = t2.taskid;
        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_done_hit_ids_by_webapp_id(self, webapp_id):
        select_sql = f'''
        select hitid from scribo_webapps_db.tasks_hits as t1
            join scribo_webapps_db.tasks as t2
        where t2.webappid = {webapp_id}
            and t1.taskID = t2.taskid
            and t1.done_by is not null;
        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_done_not_qa_hit_ids_by_webapp_id(self, webapp_id):
        select_sql = f'''
        select hitid from scribo_webapps_db.tasks_hits as t1
            join scribo_webapps_db.tasks as t2
        where t2.webappid = {webapp_id}
            and t1.taskID = t2.taskid
            and t1.done_by is not null
            and t1.qa_reviewer is null;
        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_done_qa_hit_ids_by_webapp_id(self, webapp_id):
        select_sql = f'''
        select hitid from scribo_webapps_db.tasks_hits as t1
            join scribo_webapps_db.tasks as t2
        where t2.webappid = {webapp_id}
            and t1.taskID = t2.taskid
            and t1.done_by is not null
            and t1.qa_reviewer is not null;
        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_done_qa_hit_ids_by_webapp_id_OCR(self, webapp_id):
        select_sql = f'''
        select hitid from scribo_webapps_db.tasks_hits as t1
            join scribo_webapps_db.tasks as t2
        where t2.webappid = {webapp_id}
            and t1.taskID = t2.taskid
            and t1.done_by is not null
            and t1.engineeringmc_file is null
            and t1.qa_reviewer is not null;
        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    # oak batch 4
    def get_qa_done_hits_id_webapp_id_oak(self, webapp_id, date):
        select_sql = f'''
                        select t1.HitID from scribo_webapps_db.tasks_hits as t1
                            join scribo_webapps_db.tasks as t2
                        where t2.webappid ={webapp_id}
                            and t1.taskID = t2.taskid
                            and t1.qa_reviewer is not null
                            and t1.qa_submit_time > '{date}';
                        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_qa_done_hits_id_by_webapp_id(self, webapp_id, start_date='1970-01-01', end_date='9999-12-31'):
        select_sql = f'''
                        select t1.HitID from scribo_webapps_db.tasks_hits as t1
                            join scribo_webapps_db.tasks as t2
                        where t2.webappid ={webapp_id}
                            and t1.taskID = t2.taskid
                            and t1.qa_reviewer is not null
                            and t1.qa_submit_time > '{start_date}'
                            and t1.qu_submit_time < '{end_date}';
                        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_production_done_hits_id_by_webapp_id(self, webapp_id, start_date='1970-01-01', end_date='9999-12-31'):
        select_sql = f'''
                        select t1.HitID from scribo_webapps_db.tasks_hits as t1
                            join scribo_webapps_db.tasks as t2
                        where t2.webappid ={webapp_id}
                            and t1.taskID = t2.taskid
                            and t1.done_by is not null
                            and t1.submit_time > '{start_date}'
                            and t1.submit_time < '{end_date}';
                        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None

    def get_datahandled_hits_id_webapp_id_oak(self, webapp_id, date):
        select_sql = f'''
                        select t1.HitID from scribo_webapps_db.tasks_hits as t1
                            join scribo_webapps_db.tasks as t2
                        where t2.webappid ={webapp_id}
                            and t1.taskID = t2.taskid
                            and t1.done_by is not null
                            and t1.submit_time > '{date}';
                        '''
        result = self.execute_select_sql(select_sql)
        id_list = []
        if len(result) > 0:
            for item in result:
                id_list.append(item[0])
            return id_list
        else:
            return None


    def get_ringqa_contact_ids(self):
        webappids_list = []
        for key, value in config.ring_qa_webappid_dict.items():
            if value != 0:
                webappids_list.append(value)
        contact_id_list = []
        for webappid in webappids_list:
            select_sql = f'''
                            select t1.FileURL from scribo_webapps_db.tasks_hits as t1
                                            join scribo_webapps_db.tasks as t2
                                        where t2.webappid = {webappid}
                                            and t1.taskID = t2.taskid;
                            '''
            result = self.execute_select_sql(select_sql)
            if len(result) > 0:
                for item in result:
                    contact_id_list.append(item[0].split('.')[0])
        return contact_id_list
