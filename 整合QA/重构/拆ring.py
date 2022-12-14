# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 拆ring.py
@Author : wenjing
@Date : 2022/12/5 17:34
"""
import os, time, json
import sys
from pathlib import Path
sys.path.append(str(Path(f"{Path(__file__).parent.parent}/Utilities")))
import DBUtility as dbu
import DatetimeUtility as dtu
import AzureUtility as azu
from LoggingUtility import LogInit
from DatetimeUtility import now, strtoday
import ConstConfig as config
logger = LogInit('Ring_QA')


def create_tasks_hits(project_list):
    eng_db = dbu.OneForma("RINGQA")
    # onfroma_db = dbu.OneForma("Test")
    oneforma_db = dbu.OneForma("MAIN")
    azure_blob = azu.RingQABlob()
    if project_list is None:
        logger.warning("No project list")
        return
    # upload_dict_list = eng_db.get_contact_info_not_uploaded()
    upload_dict_list = eng_db.get_contact_info_not_uploaded_call_center()
    if len(upload_dict_list) <= 0:
        print("No task need to upload")
        return

    blob_path = azure_blob.create_container()
    for i in range(0, len(upload_dict_list)):
        try:
            time_start = now()
            upload_dict = upload_dict_list[i]
            contact_id = upload_dict["contact_id"]
            contact_info = upload_dict["contact_info"]
            given_data = json.dumps(contact_info)
            country = upload_dict["country"]
            taskname = None
            if "ring" in project_list:
                if country == "JP":
                    taskname = f"Ring_QA_ja-{country}_{dtu.strtoday()}"
                elif country == "CA":
                    taskname = f"Ring_QA_fr-{country}_{dtu.strtoday()}"
                elif country == "DE":
                    taskname = f"Ring_QA_de-{country}_{dtu.strtoday()}"
                elif country == "AU" or country == "GB" or country == "US" or country == "ZA":
                    taskname = f"Ring_QA_en-{country}_{dtu.strtoday()}"

            if taskname is None:
                print(f"{country} not in project")
                continue
            call_center = upload_dict["call_center"]
            audio_length = upload_dict["audio_length"]
            speech_length = upload_dict["speech_length"]
            '''
            contact_info
            def get_audio_path_by_contact_id_call_center(self, contact_id):
                try:
                    select_sql = f"SELECT audio_path FROM call_center where contact_id = '{contact_id}';"
                    result = self.execute_select_sql(select_sql)
                    if len(result) > 0:
                        return result[0][0]
                    return None
                except Exception as e:
                    print(e)
                    raise
            '''
            # audio_path = eng_db.get_audio_path_by_contact_id(contact_id)
            audio_path = eng_db.get_audio_path_by_contact_id_call_center(contact_id)
            azure_blob.upload_file_to_blob_file_path(contact_id, audio_path)
            b_upload = oneforma_db.create_audio_hit_ring_qa(
                task_name=taskname,
                given_data=given_data,
                blob_path=blob_path,
                file_url=f"{contact_id}.wav",
                # webapp_id=config.ring_qa_webappid_dict[country],
                webapp_id=eng_db.get_webappid_call_center_webapps(country),
                ruleset=str(speech_length))
            taskid = oneforma_db.get_task_id_by_name(taskname)
            hitid = oneforma_db.get_hit_id_by_task_id_fileurl(
                taskid, f"{contact_id}.wav")
            oneforma_db.create_hit_metadata(hitid, str(audio_length))
            if b_upload:
                '''
               update contact_info
               def update_is_upload_call_center(self, contact_id, blob_path=""):
                    if blob_path == "":
                        update_sql = f"update call_center set is_upload = 1 where contact_id = '{contact_id}';"
                    else:
                        update_sql = f"update call_center set is_upload = 1, blob_path = '{blob_path}' where contact_id = '{contact_id}';"
                    return self.execute_insert_sql_no_wait(update_sql)
                '''
                # b_ret = eng_db.update_is_upload(contact_id, blob_path)
                b_ret = eng_db.update_is_upload_call_center(contact_id, blob_path)
                if b_ret:
                    time_diff = now() - time_start
                    print(
                        f"--- {i + 1}/{len(upload_dict_list)} -- {contact_id} done -- {time_diff.total_seconds()}",
                        end='\r')
                else:
                    print(
                        f"!!! {i + 1}/{len(upload_dict_list)} -- {contact_id} not set upload flag"
                    )
        except Exception as e:
            print(e)
            raise


if __name__ == "__main__":
    # scheduled_run(["ring", "vm"])
    is_run = sys.argv[1]
    if is_run == "ring":
        create_tasks_hits(["ring"])
    # if is_run == "vm":
    #     create_tasks_hits(["vm"])
    # if is_run == "ocean":
    #     create_tasks_hits(["ocean"])