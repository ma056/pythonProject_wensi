# -- coding: utf-8 --
# -- coding: utf-8 --
from itertools import count
import sys
from pathlib import Path

sys.path.append(str(Path(f"{Path(__file__).parent.parent}/Utilities")))
from datetime import datetime, timedelta
import os, time, json
import shutil
import DBUtility as dbu
import WaveUtility as wavu
import DatetimeUtility as dtu
import FileUtility as fileu
import AWSUtility as awsu
import SelenuimUtility as seleu
import AzureUtility as azu
import ConstConfig as config
from WebRTCUtility import get_speech_length, get_wav_length
from DatetimeUtility import now, strtoday
from pytz import timezone
from LoggingUtility import LogInit
import multiprocessing

logger = LogInit('Ring_QA')


def main(call_center, is_sync_history: bool = False):
    print(f"====Start process for call_center {call_center}====")
    print("0. Init Utilities")
    ## Initial all class used
    eng_db = dbu.OneForma("RINGQA")
    onfroma_Asia = dbu.OneForma("MAIN")
    aws_connect = awsu.AWSConnect(call_center)
    sele_monitor = seleu.CallCenter(call_center)
    file_operator = fileu.RingQAFileOpeartor(call_center)
    aws_s3 = awsu.AWSS3(call_center)
    file_operator.create_ringqa_folder()

    print("1. Sync from AWS S3")
    ## 同步本地下载文件夹
    aws_s3.sync_aws_s3_buckets()

    ## 计算oneforma上与S3上contact id差异及列表
    audio_files_list_in_s3 = aws_s3.get_files_name_in_s3()
    contact_id_list_in_s3 = []
    for item in audio_files_list_in_s3:
        key = item.split('/')[-1].split('.')[0].split('_')[0]
        contact_id_list_in_s3.append(key)
    contact_id_list_local = file_operator.get_all_files()
    print(f"--- Local Audios {len(contact_id_list_local)}")
    ## 去除s3 重复保存的文件
    contact_id_list_local = list(set(contact_id_list_local))
    print(f"--- Local Audios {len(contact_id_list_local)}, remove duplicates")
    contact_id_list_oneforma = onfroma_Asia.get_ringqa_contact_ids()
    if contact_id_list_oneforma == None:
        contact_id_list_oneforma = []
    print(f"--- Onforma Audios {len(contact_id_list_oneforma)}")
    contact_id_in_engserver = eng_db.get_contact_ids_from_engserver()
    new_contact_id_list = []
    for contact_id_local in contact_id_list_local:
        if contact_id_local not in contact_id_list_oneforma and contact_id_local not in contact_id_in_engserver:
            new_contact_id_list.append(contact_id_local)
    print(f"--- New Audios {len(new_contact_id_list)}")
    new_contact_id_list = list(set(new_contact_id_list))
    print(f"--- New Audios {len(new_contact_id_list)}, remove duplicates")
    for new_contact_id in new_contact_id_list:
        eng_db.save_new_contact_id_to_engserver(new_contact_id)
    print("2. Update Contact Info to EngServer DB")
    print("--- Get contact attributes")
    ## 如果上传历史数据为true 则先获取engserver 中的contact id
    contact_id_list_in_engserver_not_attr_get = eng_db.get_contact_ids_from_engserver_get_attr(
    )
    print(f"--- New Attr get {len(contact_id_list_in_engserver_not_attr_get)}")
    ## 调用aws API获取contact id 对应的attributes 并生产字典
    print("--- Get attrs and save to db")
    for i in range(0, len(contact_id_list_in_engserver_not_attr_get)):
        try:
            time_start = now()
            contact_id = contact_id_list_in_engserver_not_attr_get[i]
            contact_attr_dict = aws_connect.get_contact_id_attr(contact_id)
            b_inserted = eng_db.save_contact_id_attr_to_engserver(
                contact_id, contact_attr_dict, call_center)
            time_diff = now() - time_start
            if b_inserted:
                print(
                    f"--- {i + 1}/{len(contact_id_list_in_engserver_not_attr_get)} update to engserver db -- {time_diff.total_seconds()}",
                    end="\r")
            else:
                print(f"!!! {contact_id} insert false")
        except Exception as e:
            logger.warning(
                f"!!! {contact_id_list_in_engserver_not_attr_get[i]} insert error: {e}"
            )
    print("--- Calculate speech length and audio length")
    all_file_list = file_operator.get_all_files_original()
    length_contact_ids = eng_db.get_contact_id_not_calculated()
    print(f"--- Calcualte Audios {len(length_contact_ids)}")

    for audio_file in all_file_list:
        for length_contact_id in length_contact_ids:
            if length_contact_id in audio_file:
                audio_path = Path(
                    f"{file_operator.audio_sync_path}/{audio_file}")
                audio_length = get_wav_length(audio_path)
                speech_length = get_speech_length(audio_path)
                eng_db.save_audiopath_audiolength_speechlength_to_engserver(
                    length_contact_id, str(audio_path), audio_length,
                    speech_length, 1)
                print(
                    f"{length_contact_id} -- {speech_length} -- {audio_length}",
                    end='\r')

    print("--- Save search result to DB")
    sele_monitor.browser_init_call_center(headless=True)
    cookies = sele_monitor.get_call_center_cookies()
    print("--- Get cookie success")
    contact_id_list_in_engserver_not_search_get = eng_db.get_contact_ids_from_engserver_get_search(call_center)
    get_attr_multi(sele_monitor, eng_db, contact_id_list_in_engserver_not_search_get, cookies, 1)
    print("--- Search result saved")


def get_attr_multi(sele_monitor, eng_db, contact_id_list, cookies, no):
    if no > 1:
        m_contact_id_list = list_slice(contact_id_list, no)
        tasks_pool = multiprocessing.Pool(processes=no)
        for i in range(0, len(m_contact_id_list)):
            t_contact_id_list = m_contact_id_list[i]
            print(f"Process {i + 1} queue length {len(t_contact_id_list)}")
            tasks_pool.apply_async(get_call_center_attr, args=(sele_monitor, eng_db, t_contact_id_list, cookies, i))
        tasks_pool.close()
        tasks_pool.join()
    else:
        get_call_center_attr(sele_monitor, eng_db, contact_id_list, cookies, 1)


def get_call_center_attr(sele_monitor, eng_db, contact_id_list, cookies, po):
    print(f"Process {po} Start")
    for i in range(0, len(contact_id_list)):
        try:
            time_start = now()
            contact_id = contact_id_list[i]
            attr_json = sele_monitor.get_attr_from_call_center(contact_id, cookies)
            attr_json_dict = json.loads(attr_json)
            if attr_json_dict.get('ctrDetails') is None:
                print(f"{contact_id} failed to Get attr")
                continue
            system_number = attr_json_dict.get('ctrDetails').get('SystemEndpoint').get('Address')
            customer_number = attr_json_dict.get('ctrDetails').get('CustomerEndpoint').get('Address')
            disconnect_timestamp = attr_json_dict.get('ctrDetails').get('DisconnectTimestamp').replace('T',
                                                                                                       ' ').replace('Z',
                                                                                                                    '')
            contact_duration = attr_json_dict.get('ctrDetails').get('Queue').get('Duration')
            contact_search_result = {
                "Contact ID": contact_id,
                "System phone number": system_number,
                "Customer phone number": customer_number,
                "Disconnect timestamp": disconnect_timestamp,
                "Contact duration": str(contact_duration),
            }
            eng_db.save_contact_search_result_to_engserver(
                contact_search_result)
            time_diff = now() - time_start
            print(
                f"--- {po} {i + 1}/{len(contact_id_list)} -- {contact_id} updated -- {time_diff.total_seconds()}",
                end="\n")
        except Exception as e:
            print(
                f"!!! {contact_id_list[i]} insert error"
            )
            print(e)
    print(f"Process {po} End")


def list_slice(list, no):
    no = int(no)
    step = int(len(list) / no)
    new_list = []
    for i in range(0, no):
        if i == no - 1:
            temp_list = list[i * step:]
        else:
            temp_list = list[i * step:i * step + step]
        new_list.append(temp_list)
    return new_list


def create_tasks_hits(project_list):
    eng_db = dbu.OneForma("RINGQA")
    # onfroma_db = dbu.OneForma("Test")
    oneforma_db = dbu.OneForma("MAIN")
    azure_blob = azu.RingQABlob()
    if project_list is None:
        logger.warning("No project list")
        return
    upload_dict_list = eng_db.get_contact_info_not_uploaded()
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
            if "vm" in project_list:
                if country == "VMIDENSP" or country == "VMIDHIEN" or country == "VMIDFRGE" or country == "VMIDENFR" or country == "VMIDHITA":
                    taskname = f"VocieMail_LangID_Collection_{country[-4:]}_{dtu.strtoday()}"
            if "ring" in project_list:
                if country == "JP":
                    taskname = f"Ring_QA_ja-{country}_{dtu.strtoday()}"
                elif country == "CA":
                    taskname = f"Ring_QA_fr-{country}_{dtu.strtoday()}"
                elif country == "DE":
                    taskname = f"Ring_QA_de-{country}_{dtu.strtoday()}"
                elif country == "AU" or country == "GB" or country == "US" or country == "ZA":
                    taskname = f"Ring_QA_en-{country}_{dtu.strtoday()}"
            if "ocean" in project_list:
                if country == "OVMAR" or country == "OVMFI" or country == "OVMNO" or country == "OVMSW":
                    taskname = f"Ocean_Voicemail_{country[-2:]}_{dtu.strtoday()}"
                    ocean_gender_dict = {
                        "1": "Man",
                        "2": "Woman",
                    }
                    ocean_background_dict = {
                        "1": "Home_TV-Music-off",
                        "2": "Home_Music-on",
                        "3": "Home_TV-on",
                        "4": "Coffee-Shop",
                        "5": "Restaurant",
                        "6": "Office",
                        "7": "Commercial",
                        "8": "Street",
                    }
                    ocean_topics_dict = {
                        "1": "Casual",
                        "2": "Business",
                    }
                    ocean_make_dict = {
                        "1": "Iphone",
                        "2": "Samsung Phone",
                        "3": "Huawei Phone",
                        "4": "Xiaomi Phone",
                        "5": "LG Phone",
                        "6": "Another Android Device",
                        "7": "Others",
                    }

                    ocean_gender = ocean_gender_dict.get(contact_info.get('mobile_type'))
                    if ocean_gender is None:
                        ocean_gender = "Error"

                    ocean_background = ocean_background_dict.get(contact_info.get('call_type'))
                    if ocean_background is None:
                        ocean_background = "Error"

                    ocean_topics = ocean_topics_dict.get(contact_info.get('background'))
                    if ocean_topics is None:
                        ocean_topics = "Error"

                    ocean_make = ocean_make_dict.get(contact_info.get('voip'))
                    if ocean_make is None:
                        ocean_make = "Error"

                    temp_contact_info = {
                        "Contact_ID": contact_info.get('contactid'),
                        "System_phone_number": contact_info.get('System_phone_number'),
                        "Customer_phone_number": contact_info.get('telephone_number'),
                        "Disconnect_timestamp": contact_info.get('date'),
                        "Contact_duration": contact_info.get('Contact_duration'),
                        "Gender": ocean_gender,
                        "Gender_Input": contact_info.get('mobile_type'),
                        "Background_noise": ocean_background,
                        "Background_noise_Input": contact_info.get('call_type'),
                        "Topics": ocean_topics,
                        "Topics_Input": contact_info.get('background'),
                        "Make": ocean_make,
                        "Make_Input": contact_info.get('voip'),
                        "oneforma_id": contact_info.get('oneforma_id'),
                    }
                    given_data = json.dumps(temp_contact_info)
            if taskname is None:
                print(f"{country} not in project")
                continue
            call_center = upload_dict["call_center"]
            audio_length = upload_dict["audio_length"]
            speech_length = upload_dict["speech_length"]
            audio_path = eng_db.get_audio_path_by_contact_id(contact_id)
            azure_blob.upload_file_to_blob_file_path(contact_id, audio_path)
            b_upload = oneforma_db.create_audio_hit_ring_qa(
                task_name=taskname,
                given_data=given_data,
                blob_path=blob_path,
                file_url=f"{contact_id}.wav",
                webapp_id=config.ring_qa_webappid_dict[country],
                ruleset=str(speech_length))
            taskid = oneforma_db.get_task_id_by_name(taskname)
            hitid = oneforma_db.get_hit_id_by_task_id_fileurl(
                taskid, f"{contact_id}.wav")
            oneforma_db.create_hit_metadata(hitid, str(audio_length))
            if b_upload:
                b_ret = eng_db.update_is_upload(contact_id, blob_path)
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


def Run():
    main("US", False)
    main("AU", False)
    main("JP", False)


def status_update():
    update_is_upload()


def update_is_upload():
    onfroma_Asia = dbu.OneForma("Main")
    eng_db = dbu.OneForma("RINGQA")
    contact_id_list_oneforma = onfroma_Asia.get_ringqa_contact_ids()
    contact_id_list_in_engserver = eng_db.get_contact_ids_from_engserver()
    if contact_id_list_oneforma is None:
        contact_id_list_oneforma = []
    for i in range(0, len(contact_id_list_oneforma)):
        contact_id = contact_id_list_oneforma[i]
        if contact_id in contact_id_list_in_engserver:
            b_ret = eng_db.update_is_upload(contact_id)
            if not b_ret:
                print(f"!!! {contact_id} fail")
        print(
            f"--- {i + 1}/{len(contact_id_list_oneforma)} -- {contact_id} Done",
            end="\r")


def Get_hit_numbers():
    dbo = dbu.OneForma("Main")
    taskname_base_list = [
        "Ring_QA_ja-JP_",
        "Ring_QA_en-AU_",
        "Ring_QA_en-US_",
        "Ring_QA_fr-CA_",
        "Ring_QA_en-GB_",
        "Ring_QA_de-DE_",
        "Ring_QA_en-ZA_",
    ]
    taskname_list = []
    print(" ")
    for taskbasename in taskname_base_list:
        taskname_list.append(f"{taskbasename}{strtoday()}")
    for taskname in taskname_list:
        taskid = dbo.get_task_id_by_name(taskname)
        if taskid is not None:
            hits = dbo.get_hits_id_by_task_id(taskid)
            hit_number = len(hits)
            print(f"{taskname} : {hit_number}")


def scheduled_run(project_list):
    Run()
    status_update()
    create_tasks_hits(project_list)
    Get_hit_numbers()
    import VoiceMail_LanguageID_Main
    VoiceMail_LanguageID_Main.main()


if __name__ == "__main__":
    # scheduled_run(["ring", "vm"])
    is_run = sys.argv[1]
    if is_run == "ring":
        scheduled_run(["ring"])
    if is_run == "vm":
        scheduled_run(["vm"])
    if is_run == "ocean":
        scheduled_run(["ocean"])

