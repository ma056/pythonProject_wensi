from itertools import count
import sys
from pathlib import Path

sys.path.append(str(Path(f"{Path(__file__).parent.parent}/Utilities")))
import os, time, json
import DBUtility as dbu
import FileUtility as fileu
import AWSUtility as awsu
import SelenuimUtility as seleu
from DatetimeUtility import now, strtoday
from LoggingUtility import LogInit
import multiprocessing

logger = LogInit('Ring_QA')


def main(call_center, is_sync_history: bool = False):
    print(f"====Start process for call_center {call_center}====")
    print("0. Init Utilities")
    eng_db = dbu.OneForma("RINGQA")
    onfroma_Asia = dbu.OneForma("MAIN")
    aws_connect = awsu.AWSConnect(call_center)
    sele_monitor = seleu.CallCenter(call_center)
    file_operator = fileu.RingQAFileOpeartor(call_center)
    aws_s3 = awsu.AWSS3(call_center)

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

    '''
    涉及表call_center
    '''
    contact_id_in_engserver = eng_db.get_contact_ids_from_engserver_call_center()
    new_contact_id_list = []
    for contact_id_local in contact_id_list_local:
        if contact_id_local not in contact_id_list_oneforma and contact_id_local not in contact_id_in_engserver:
            new_contact_id_list.append(contact_id_local)
    print(f"--- New Audios {len(new_contact_id_list)}")
    new_contact_id_list = list(set(new_contact_id_list))
    print(f"--- New Audios {len(new_contact_id_list)}, remove duplicates")
    '''
    涉及表call_center
    '''
    for new_contact_id in new_contact_id_list:
        eng_db.save_new_contact_id_to_engserver_call_center(new_contact_id)
    print("2. Update Contact Info to EngServer DB")
    print("--- Get contact attributes")

    ### get 呼叫中心的属性atr
    ## 如果上传历史数据为true 则先获取engserver 中的contact id
    '''
    涉及表call_center
    '''
    contact_id_list_in_engserver_not_attr_get = eng_db.get_contact_ids_from_engserver_get_attr()
    print(f"--- New Attr get {len(contact_id_list_in_engserver_not_attr_get)}")
    ## 调用aws API获取contact id 对应的attributes 并生产字典
    print("--- Get attrs and save to db")
    for i in range(0, len(contact_id_list_in_engserver_not_attr_get)):
        try:
            time_start = now()
            contact_id = contact_id_list_in_engserver_not_attr_get[i]
            contact_attr_dict = aws_connect.get_contact_id_attr(contact_id)
            '''
            涉及表call_center
            '''
            b_inserted = eng_db.save_contact_id_attr_to_engserver_call_center(contact_id, contact_attr_dict,
                                                                              call_center)
            time_diff = now() - time_start
            if b_inserted:
                print(
                    f"--- {i + 1}/{len(contact_id_list_in_engserver_not_attr_get)} update to engserver db -- {time_diff.total_seconds()}",
                    end="\r")
            else:
                print(f"!!! {contact_id} insert false")
        except Exception as e:
            logger.warning(f"!!! {contact_id_list_in_engserver_not_attr_get[i]} insert error: {e}")
    print("--- Calculate speech length and audio length")

    # get呼叫中心得属性 通过selenium库来爬取
    sele_monitor.browser_init_call_center(headless=True)
    cookies = sele_monitor.get_call_center_cookies()
    print("--- Get cookie success")
    '''
    涉及表call_center
    '''
    contact_id_list_in_engserver_not_search_get = eng_db.get_contact_ids_from_engserver_get_search_call_center(
        call_center)
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
            '''
            涉及表call_center
            '''
            eng_db.save_contact_search_result_to_engserver_call_center(contact_search_result)
            time_diff = now() - time_start
            print(f"--- {po} {i + 1}/{len(contact_id_list)} -- {contact_id} updated -- {time_diff.total_seconds()}",
                  end="\n")
        except Exception as e:
            print(f"!!! {contact_id_list[i]} insert error")
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
