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


class Mysql(DBOperator):
    def __init__(self, db_name: DB_Name):
        super().__init__(db_name)
        self.is_open = self.open_database()

    def get_new_info_by_userid(self, userid):
        select_sql = f"select * from worldwide_info where UserId = '{userid}'"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def gracetitles_insert_start_info(self, filter_hitid, filter_taskid, filename, file_path):
        filename = self.escape_string(filename)
        file_path = self.escape_string(file_path)
        insert_sql = f"insert into gracetitles_info (filter_hitid, filter_taskid, file_name, filepath) values ({filter_hitid}, {filter_taskid}, '{filename}', '{file_path}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_insert_error_qa_data(self, hitid, fileurl, qa_data, ip):
        fileurl = self.escape_string(fileurl)
        qa_data = self.escape_string(qa_data)
        insert_sql = f"replace into gracetitles_error_qadata (hitid, fileurl, qa_data, Source_IP) values ({hitid}, '{fileurl}', '{qa_data}', '{ip}');"
        self.execute_insert_sql_no_wait(insert_sql)


    def gracetitles_insert_bi(self, file_name, taskid, taskname, hitid, done_by, qa_reviewer, qa_result, qa_domain, audio_length, qa_commnets, is_pay):
        file_name = self.escape_string(file_name)
        qa_commnets = self.escape_string(qa_commnets)
        select_sql = f"select id from gracetitles_bi where hitid = {hitid};"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            id = result[0][0]
            insert_sql = f"update gracetitles_bi set file_name = '{file_name}', taskid = '{taskid}', taskname = '{taskname}', hitid = '{hitid}', done_by = '{done_by}', qa_reviewer = '{qa_reviewer}', qa_result = '{qa_result}', qa_domain = '{qa_domain}', audio_length = '{audio_length}', qa_comments = '{qa_commnets}', is_pay = '{is_pay}' where id = {id};"
        else:
            insert_sql = f"insert into gracetitles_bi (file_name, taskid, taskname, hitid, done_by, qa_reviewer, qa_result, qa_domain, audio_length, qa_comments, is_pay) values ('{file_name}', '{taskid}', '{taskname}', '{hitid}', '{done_by}', '{qa_reviewer}', '{qa_result}', '{qa_domain}', '{audio_length}', '{qa_commnets}', '{is_pay}');"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_insert_judge(self, file_name, filter_judge):
        file_name = self.escape_string(file_name)
        select_sql = f"select id from gracetitles_judge where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result) > 0:
            id = result[0][0]
            insert_sql = f"update gracetitles_judge set judge = '{filter_judge}' where id = {id};"
        else:
            insert_sql = f"insert into gracetitles_judge (file_name, judge) values ('{file_name}', '{filter_judge}');"
        self.execute_insert_sql_no_wait(insert_sql)


    def gracetitles_update_filter_info(self, filter_hitid, filter_taskid, filename, filter_judge, filter_commnet, status):
        filter_commnet = self.escape_string(filter_commnet)
        filename = self.escape_string(filename)
        insert_sql = f"update gracetitles_info set filter_hitid = {filter_hitid}, filter_taskid = {filter_taskid}, filter_judge = '{filter_judge}', filter_comment = '{filter_commnet}', status = '{status}' where file_name = '{filename}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_pro_info(self, pro_hitid, pro_taskid, filename, status):
        filename = self.escape_string(filename)
        insert_sql = f"update gracetitles_info set pro_hitid = '{pro_hitid}', pro_taskid = {pro_taskid}, status = '{status}', is_pro=1 where file_name = '{filename}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_error_info(self, filename, error):
        filename = self.escape_string(filename)
        insert_sql = f"update gracetitles_info set error = '{error}', status = 'error' where file_name = '{filename}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_file_path(self, filename, file_path):
        filename = self.escape_string(filename)
        file_path = self.escape_string(file_path)
        insert_sql = f"update gracetitles_info set filepath = '{file_path}' where file_name = '{filename}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_status_by_pro_taskid(self, taskid, status):
        insert_sql = f"update gracetitles_info set status = '{status}' where pro_taskid = '{taskid}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_status_by_file_name(self, file_name, status):
        insert_sql = f"update gracetitles_info set status = '{status}' where file_name = '{file_name}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_qa_time_by_file_name(self, file_name, qa_time):
        insert_sql = f"update gracetitles_info set qa_time = '{qa_time}' where file_name = '{file_name}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_meeting_category_by_file_name(self, file_name, meeting_category):
        meeting_category = self.escape_string(meeting_category)
        insert_sql = f"update gracetitles_info set meeting_category = '{meeting_category}' where file_name = '{file_name}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_bi_sync(self, filename, bi_sync):
        filename = self.escape_string(filename)
        insert_sql = f"update gracetitles_info set bi_sync = '{bi_sync}' where file_name = '{filename}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_is_delivery(self, filename, is_dlivery):
        filename = self.escape_string(filename)
        insert_sql = f"update gracetitles_info set is_delivery = '{is_dlivery}' where file_name = '{filename}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_is_pro_audio_length(self, filename, is_pro, audio_length):
        filename = self.escape_string(filename)
        insert_sql = f"update gracetitles_info set is_pro = {is_pro}, audio_length = '{audio_length}' where file_name = '{filename}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_update_audio_length_by_id(self, id, audio_length):
        insert_sql = f"update gracetitles_info set audio_length = '{audio_length}' where id = '{id}';"
        self.execute_insert_sql_no_wait(insert_sql)

    def gracetitles_get_qa_ed_file_name(self):
        select_sql = f"select file_name from gracetitles_info where status = 'qa' and is_delivery = 0 and remove = 0 and reassign = 0;"
        result = self.execute_select_sql(select_sql)
        file_name_list = []
        if len(result)>0:
            for item in result:
                file_name_list.append(item[0])
            return file_name_list
        else:
            return []

    def gracetitles_get_error_file_name(self):
        select_sql = f"select file_name from gracetitles_info where is_delivery = 8;"
        result = self.execute_select_sql(select_sql)
        file_name_list = []
        if len(result)>0:
            for item in result:
                file_name_list.append(item[0])
            return file_name_list
        else:
            return []

    def gracetitles_get_error_hit_from_tecentdb(self):
        select_sql = f"select id from gracetitles_error_qadata where Completed = 5;"
        result = self.execute_select_sql(select_sql)
        file_name_list = []
        if len(result)>0:
            for item in result:
                file_name_list.append(item[0])
            return file_name_list
        else:
            return []

    def gracetitles_get_chapter_error_file_name(self):
        select_sql = f"select file_name from gracetitles_info where is_delivery = 7;"
        result = self.execute_select_sql(select_sql)
        file_name_list = []
        if len(result)>0:
            for item in result:
                file_name_list.append(item[0])
            return file_name_list
        else:
            return []

    def gracetitles_get_file_path_by_file_name(self, file_name):
        select_sql = f"select filepath from gracetitles_info where file_name = '{file_name}' "
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0][0]
        else:
            return None

    def gracetitles_get_meeting_category_by_file_name(self, file_name):
        select_sql = f"select meeting_category from gracetitles_info where file_name = '{file_name}' "
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0][0]
        else:
            return None


    def gracetitles_get_file_path_list(self):
        select_sql = f"select filepath from gracetitles_info"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_offline_rework_data(self, hitid):
        select_sql = f"select qa_data, fileurl from gracetitles_error_qadata where hitid = {hitid} and Completed = 1"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0]
        else:
            return None

    def gracetitles_get_offline_rework_data_by_id(self, id):
        select_sql = f"select qa_data, fileurl, hitid from gracetitles_error_qadata where id = {id}"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0]
        else:
            return None

    def gracetitles_get_bi_file_name_list_by_bi_sync(self, bi_sync):
        select_sql = f"select file_name from gracetitles_info where bi_sync = {bi_sync}"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_file_name_list(self):
        select_sql = f"select file_name from gracetitles_info"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_filter_hitid_list(self):
        select_sql = f"select filter_hitid from gracetitles_info"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_filter_need_update_file_name_list(self):
        select_sql = f"select file_name from gracetitles_info where filter_judge = 'Not finished' or filter_judge is null;"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_pro_need_update_file_name_list(self):
        select_sql = f"select file_name from gracetitles_info where is_pro=1 and filter_judge = 'Structured' and status = 'waitproduction';"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_pro_done_file_name_list(self):
        select_sql = f"select file_name from gracetitles_info where is_pro=1 and is_delivery = 0 and filter_judge = 'Structured';"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_qa_need_update_file_name_list(self):
        select_sql = f"select file_name from gracetitles_info where is_pro=1 and is_delivery = 0 and filter_judge = 'Structured';"
        result = self.execute_select_sql(select_sql)
        file_path_list = []
        if len(result)>0:
            for item in result:
                file_path_list.append(item[0])
            return file_path_list
        else:
            return []

    def gracetitles_get_pro_upload_info(self):
        select_sql = f"select filter_taskid, file_name, filepath from gracetitles_info where is_pro = 0 and filter_judge = 'Structured' and status = 'waitproduction'"
        result = self.execute_select_sql(select_sql)
        info_list = []
        if len(result)>0:
            for item in result:
                info_list.append(item)
            return info_list
        else:
            return []

    def gracetitles_get_pro_hitid_by_filename(self, file_name):
        select_sql = f"select pro_hitid from gracetitles_info where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0][0]
        else:
            return None

    def gracetitles_get_filter_hitid_by_filename(self, file_name):
        select_sql = f"select filter_hitid from gracetitles_info where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0][0]
        else:
            return None


    def gracetitles_get_meeting_category_by_filename(self, file_name):
        select_sql = f"select meeting_category from gracetitles_info where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0][0]
        else:
            return None

    def gracetitles_get_bi_info_by_file_name(self, file_name):
        select_sql = f"select pro_hitid, pro_taskid, audio_length, filter_judge from gracetitles_info where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0]
        else:
            return []

    def gracetitles_get_delivery_time_remark_by_file_name(self, file_name):
        select_sql = f"select delivery_time, remark from gracetitles_info where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0]
        else:
            return []

    def gracetitles_get_id_by_file_name(self, file_name):
        select_sql = f"select id from gracetitles_info where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0][0]
        else:
            return None

    def gracetitles_get_bi_qa_result_by_file_name(self, file_name):
        select_sql = f"select qa_result from gracetitles_bi where file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return result[0]
        else:
            return []

    def gracetitles_get_audio_length_is_zero(self):
        select_sql = f"select pro_hitid, id from gracetitles_info where audio_length = 0;"
        result = self.execute_select_sql(select_sql)
        info_list = []
        if len(result)>0:
            for item in result:
                info_list.append(item)
            return info_list
        else:
            return []

    def cupcakes_insert_new_form(self, topic, template_name, subtitle, label1, label2, label3, label4, label5, label6, scenario_description, filling_link, num_cut, form_id, no, collaborate_link):
        subtitle = self.escape_string(subtitle)
        scenario_description = self.escape_string(scenario_description)
        filling_link = self.escape_string(filling_link)
        collaborate_link =  self.escape_string(collaborate_link)
        template_name= self.escape_string(template_name)
        topic = self.escape_string(topic)
        insert_sql = f"INSERT INTO `helios`.`cupcakes_json` (`topic`, `template_name`, `subtitle`, `label1`, `label2`, `label3`, `label4`, `label5`, `label6`, `scenario_description`, `filling_link`, `num_cut`, `form_id`, `no`, `collaborate_link`) VALUES ('{topic}', '{template_name}', '{subtitle}', '{label1}', '{label2}', '{label3}', '{label4}', '{label5}', '{label6}', '{scenario_description}', '{filling_link}', '{num_cut}', '{form_id}', '{no}', '{collaborate_link}');"
        result = self.execute_insert_sql_no_wait(insert_sql)

    def cupcakes_query_insert_new_form(self, topic, template_name, subtitle, label1, label2, label3, label4, label5, label6, scenario_description, filling_link, num_cut, form_id, no):
        subtitle = self.escape_string(subtitle)
        scenario_description = self.escape_string(scenario_description)
        filling_link = self.escape_string(filling_link)
        template_name= self.escape_string(template_name)
        topic = self.escape_string(topic)
        insert_sql = f"INSERT INTO `helios`.`cupcakes_query` (`topic`, `template_name`, `subtitle`, `label1`, `label2`, `label3`, `label4`, `label5`, `label6`, `scenario_description`, `filling_link`, `num_cut`, `form_id`, `no`) VALUES ('{topic}', '{template_name}', '{subtitle}', '{label1}', '{label2}', '{label3}', '{label4}', '{label5}', '{label6}', '{scenario_description}', '{filling_link}', '{num_cut}', '{form_id}', '{no}');"
        result = self.execute_insert_sql_no_wait(insert_sql)

    def cupcakes_get_download_form_ids(self):
        select_sql = f"SELECT form_id FROM helios.cupcakes_json where is_download = 0 and form_id != '404';"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item[0])
            return reuslt_list
        else:
            return []

    def cupcakes_get_all_form_ids(self):
        select_sql = f"SELECT form_id FROM helios.cupcakes_json;"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item[0])
            return reuslt_list
        else:
            return []

    def cupcakes_get_page_url_by_id(self, formid):
        select_sql = f"SELECT filling_link FROM helios.cupcakes_json where form_id = '{formid}';"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item[0])
            return reuslt_list
        else:
            return []

    def cupcakes_get_all_not_answer_connect_info(self):
        select_sql = f"SELECT form_id,orgid,onwerid,isgroup,collaborate_link FROM helios.cupcakes_json where answer_get = 0;"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
            return reuslt_list
        else:
            return []

    def cupcakes_query_get_download_form_ids(self):
        select_sql = f"SELECT form_id FROM helios.cupcakes_query where is_download = 0 and form_id != '404';"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item[0])
            return reuslt_list
        else:
            return []
    def cupcakes_update_answer_get_answer_path(self,form_id,answer_path):
        answer_path = self.escape_string(answer_path)
        update_sql = f"UPDATE `helios`.`cupcakes_json` SET `answer_get` = 1, `answer_path` = '{answer_path}' WHERE (`form_id` = '{form_id}');"
        result = self.execute_insert_sql_no_wait(update_sql)

    def cupcakes_update_download_result(self, is_download, json_path, form_id):
        json_path = self.escape_string(json_path)
        update_sql = f"UPDATE `helios`.`cupcakes_json` SET `is_download` = '{is_download}', `json_path` = '{json_path}' WHERE (`form_id` = '{form_id}');"
        result = self.execute_insert_sql_no_wait(update_sql)

    def cupcakes_update_is_delivery(self, is_delivery, form_id):
        update_sql = f"UPDATE `helios`.`cupcakes_json` SET `is_delivery` = '{is_delivery}' WHERE (`form_id` = '{form_id}');"
        result = self.execute_insert_sql_no_wait(update_sql)

    def cupcakes_update_download_result_V2(self, is_download, json_path, is_answer_get, answer_path, form_id):
        json_path = self.escape_string(json_path)
        answer_path = self.escape_string(answer_path)
        update_sql = f"UPDATE `helios`.`cupcakes_json` SET `is_download` = '{is_download}', `json_path` = '{json_path}', `answer_get` = '{is_answer_get}', `answer_path` = '{answer_path}' WHERE (`form_id` = '{form_id}');"
        result = self.execute_insert_sql_no_wait(update_sql)

    def cupcakes_query_update_download_result(self, is_download, json_path, form_id):
        json_path = self.escape_string(json_path)
        update_sql = f"UPDATE `helios`.`cupcakes_query` SET `is_download` = '{is_download}', `json_path` = '{json_path}' WHERE (`form_id` = '{form_id}');"
        result = self.execute_insert_sql_no_wait(update_sql)

    def cupcakes_update_search_result(self, search_result, form_id, is_delivery = 9):
        search_result = self.escape_string(search_result)
        update_sql = f"UPDATE `helios`.`cupcakes_json` SET `is_delivery` = {is_delivery}, `search_result` = '{search_result}' WHERE (`form_id` = '{form_id}');"
        result = self.execute_insert_sql_no_wait(update_sql)

    def cupcakes_query_update_search_result(self, search_result, form_id, is_delivery = 9):
        search_result = self.escape_string(search_result)
        update_sql = f"UPDATE `helios`.`cupcakes_query` SET `is_delivery` = {is_delivery}, `search_result` = '{search_result}' WHERE (`form_id` = '{form_id}');"
        result = self.execute_insert_sql_no_wait(update_sql)

    def cupcakes_get_downloaded_form_info(self):
        select_sql = f"SELECT `template_name`, `label1`, `label2`, `label3`, `label4`, `label5`, `label6`, `num_cut`, `json_path`, `form_id`, `no` FROM helios.cupcakes_json where is_download = 1 and is_delivery = 0;"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
        return reuslt_list

    def cupcakes_get_search_result(self, id_lower, id_upper):
        select_sql = f"SELECT `search_result`,`template_name` FROM helios.cupcakes_json where id >= {id_lower} and id <= {id_upper};"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
        return reuslt_list

    def cupcakes_query_get_search_result(self, id_lower, id_upper):
        select_sql = f"SELECT `search_result`,`template_name` FROM helios.cupcakes_query where id >= {id_lower} and id <= {id_upper};"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
        return reuslt_list

    def cupcakes_get_downloaded_query_info(self):
        select_sql = f"SELECT `json_path`, `form_id`, `filling_link` FROM helios.cupcakes_json where is_download = 1 and is_delivery = 0;"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
        return reuslt_list

    def cupcakes_query_get_downloaded_query_info(self):
        select_sql = f"SELECT `json_path`, `form_id`, `filling_link` FROM helios.cupcakes_query where is_download = 1 and is_delivery = 0;"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
        return reuslt_list

    def cupcakes_get_downloaded_query_info_subtitle(self):
        select_sql = f"SELECT `json_path`, `form_id`, `filling_link` FROM helios.cupcakes_json where is_download = 1;"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
        return reuslt_list

    def ted_talk_create_new(self, category, topic, title, url):
        title = self.escape_string(title)
        url = self.escape_string(url)
        insert_sql = f"INSERT INTO helios.ted_talks_db (category, topic, title, url) VALUES ('{category}','{topic}', '{title}', '{url}')"
        self.execute_insert_sql_no_wait(insert_sql)

    def ted_talk_update_language_file_path(self, id, languages,languages_no, file_path):
        file_path = self.escape_string(file_path)
        insert_sql = f"UPDATE helios.ted_talks_db t SET t.file_path = '{file_path}', t.languages = '{languages}', t.languages_no = '{languages_no}' WHERE t.id = {id}"
        self.execute_insert_sql_no_wait(insert_sql)

    def ted_talk_title_exists(self, title):
        title = self.escape_string(title)
        select_sql = f"SELECT * FROM helios.ted_talks_db where title = '{title}';"
        result = self.execute_select_sql(select_sql)
        if len(result)>0:
            return len(result)
        else:
            return 0

    def ted_talk_get_crawle_list(self, languages_limit=0):
        if languages_limit == 0:
            select_sql = f"SELECT id, url FROM helios.ted_talks_db where languages_no = 0;"
        else:
            select_sql = f"SELECT id, url FROM helios.ted_talks_db where languages_no < {languages_limit};"
        result = self.execute_select_sql(select_sql)
        reuslt_list = []
        if len(result)>0:
            for item in result:
                reuslt_list.append(item)
        return reuslt_list

    def scrappy_get_all_hitids(self):
        select_sql = f"select hitid from scrappy;"
        result = self.execute_select_sql(select_sql)
        info_list = []
        if len(result)>0:
            for item in result:
                info_list.append(item[0])
            return info_list
        else:
            return []

    def scrappy_insert_hitid(self, hitid, task_id, task_name, file_url):
        insert_sql = f"INSERT INTO `helios`.`scrappy` (`image_name`, `hitid`, `taskid`, `taskname`) VALUES ('{file_url}', '{hitid}', '{task_id}', '{task_name}');"
        return self.execute_insert_sql_no_wait(insert_sql)

    def scrappy_get_need_update_ids(self):
        select_sql = f"select id, image_name, taskname from scrappy where image_path is NULL;"
        result = self.execute_select_sql(select_sql)
        info_list = []
        if len(result)>0:
            for item in result:
                info_list.append(item)
            return info_list
        else:
            return []

    def scrappy_update_image_path(self, id, image_path):
        image_path = self.escape_string(image_path)
        update_sql = f"UPDATE `helios`.`scrappy` SET `image_path` = '{image_path}' WHERE (`id` = {id});"
        return self.execute_insert_sql_no_wait(update_sql)

    def scrappy_get_not_annotated_hitids(self):
        select_sql = f"select hitid from scrappy where qa_annotation is NULL;"
        result = self.execute_select_sql(select_sql)
        info_list = []
        if len(result)>0:
            for item in result:
                info_list.append(item[0])
            return info_list
        else:
            return []

    def scrappy_update_annotation(self, hitid, annotation_json, qa_annotation_json):
        update_sql = f"UPDATE `helios`.`scrappy` SET `annotation` = '{annotation_json}', `qa_annotation` = '{qa_annotation_json}' WHERE (`hitid` = '{hitid}');"
        return self.execute_insert_sql_no_wait(update_sql)

    def scrappy_update_delivery(self, hitid, delivery_image, delivery_xml, batch, delivery_time):
        update_sql = f'''UPDATE `helios`.`scrappy` SET 
        `is_delivery` = '1', 
        `delivery_image` = '{self.escape_string(delivery_image)}',
        `delivery_xml` = '{self.escape_string(delivery_xml)}',
        `batch` = '{self.escape_string(batch)}',
        `delivery_time` = '{delivery_time}'
        WHERE `hitid` = '{hitid}';'''
        return self.execute_insert_sql_no_wait(update_sql)

    def scrappy_get_annotated_hitids(self):
        select_sql = f"select hitid from scrappy where annotation is not null and is_delivery = 0;"
        result = self.execute_select_sql(select_sql)
        info_list = []
        if len(result)>0:
            for item in result:
                info_list.append(item[0])
            return info_list
        else:
            return []

    def scrappy_get_annotated_by_hitid(self, hitid):
        select_sql = f"select image_path, annotation, qa_annotation, taskname from scrappy where hitid = '{hitid}';"
        result = self.execute_select_sql(select_sql)
        if result is not None and len(result) == 1:
            return result[0]
        else:
            return None

    def wordcount_get_project_config(self, project_name):
        select_sql = f"select project_config from wordcount_config where project_name = '{project_name}';"
        result = self.execute_select_sql(select_sql)
        if result is not None and len(result) == 1:
            return result[0][0]
        else:
            return None


    def wordcount_insert_project_config(self, project_name, project_config):
        project_name = self.escape_string(project_name)
        project_config = self.escape_string(project_config)
        insert_sql = f"REPLACE INTO `helios`.`wordcount_config` (`project_name`, `project_config`) VALUES ('{project_name}', '{project_config}');"
        return self.execute_insert_sql_no_wait_ret_id(insert_sql)

    def wordcount_insert_main_row(self, project_name, client_id, ho_name, file_name, word_count):
        project_name = self.escape_string(project_name)
        client_id = self.escape_string(client_id)
        ho_name = self.escape_string(ho_name)
        file_name = self.escape_string(file_name)
        insert_sql = f"REPLACE INTO `helios`.`wordcount_main` (`project_name`, `client_id`, `ho_name`, `file_name`, `word_count`, `active`) VALUES ('{project_name}', '{client_id}', '{ho_name}', '{file_name}', '{word_count}', 1);"
        return self.execute_insert_sql_no_wait_ret_id(insert_sql)

    def wordcount_insert_source_row(self, main_id, source_text):
        source_text = self.escape_string(source_text)
        insert_sql = f"INSERT INTO `helios`.`wordcount_source` (`main_id`, `source_text`) VALUES ('{main_id}', '{source_text}');"
        return self.execute_insert_sql_no_wait_ret_id(insert_sql)

    def wordcount_insert_summary_row(self, project_name, ho_name, file_name, word_count):
        project_name = self.escape_string(project_name)
        ho_name = self.escape_string(ho_name)
        file_name = self.escape_string(file_name)
        select_sql = f"Select id from wordcount_summary where project_name = '{project_name}' and ho_name = '{ho_name}' and file_name = '{file_name}';"
        result = self.execute_select_sql(select_sql)
        if result is not None and len(result) == 1:
            update_sql = f"UPDATE `helios`.`wordcount_summary` SET `word_count_sum` = '{word_count}' WHERE (`id` = '{result[0][0]}');"
            return self.execute_insert_sql_no_wait(update_sql)
        else:
            insert_sql = f"INSERT INTO `helios`.`wordcount_summary` (`project_name`, `ho_name`, `file_name`, `word_count_sum`) VALUES ('{project_name}', '{ho_name}', '{file_name}', '{word_count}');"
            return self.execute_insert_sql_no_wait_ret_id(insert_sql)
