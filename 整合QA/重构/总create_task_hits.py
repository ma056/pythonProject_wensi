# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 总create_task_hits.py
@Author : wenjing
@Date : 2022/12/5 17:34
"""


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