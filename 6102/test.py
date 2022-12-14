# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : test.py
@Author : wenjing
@Date : 2022/12/6 14:52
"""
import sys
from pathlib import Path
from FileUtility import ExcelOperator, CSVOperator
sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
import os, json, time, html


def main(webappid_list,webappids):
    dbo = OneForma("Main")
    res_list = []
    for webappid in webappid_list:
        taskids = dbo.get_task_ids_by_webapp_id(webappid)
        if taskids is None:
            print("No task found")
            return
        for taskid in taskids:
            taskname = dbo.get_task_name_by_id(taskid)
            new_taskname = taskname + "_review"
            review_task_id = dbo.get_task_id_by_name(new_taskname)
            if review_task_id is not None:
                print(f"Task {taskname} already exists, skip")
                continue
            # tasks_hits种获取hits_id
            hitids = dbo.get_hits_id_by_task_id(taskid)
            for i in range(len(hitids)):
                hitid = hitids[i]
                # select qa_data from tasks_hits where hitid根据hitid获取qa_data
                qa_data = dbo.get_qadata_by_hitid(hitid)
                reason = None
                if qa_data is None:
                    status = "pending"
                    print(f"No QA data found for hit {hitid}")
                    # select data_handled from tasks_hits where hitid
                    # datahandled = dbo.get_datahandeld_by_hitid(hitid)
                    # if datahandled is None:
                    #     print(f"No data handled found for hit {hitid}")
                    #     continue
                    # hit_data = html.unescape(datahandled)
                else:
                    hit_data = html.unescape(qa_data)
                    if 'Rejection Feedback' in hit_data and type('hit_data') == 'str':
                        status = 'reject'
                        reason = hit_data.split(': ')[-1]
                    else:
                        status = 'Approve'
                data_res = dbo.get_done_by_qa_data_qa_reviewer_submittime_by_hit_id(hitid)
                done_by = data_res[0]
                qa_reviewer = data_res[2]
                qa_submit_time = data_res[4]
                res_dict = {
                    "Webapp ID": webappid,
                    "Hits ID": hitid,
                    "Hits Status(Approve/reject/pending)": status,
                    "Reject reason ": reason,
                    "Done by": done_by,
                    "QA user name": qa_reviewer,
                    "QA time": qa_submit_time
                }
                res_list.append(res_dict)
    excel_path = Path(f"H:/PipelineFTP/test/{webappids}_QA_.xlsx")
    nexo = ExcelOperator(excel_path)
    nexo.dict_to_excel(res_list)

if __name__ == "__main__":
    webappids = sys.argv[1]
    if webappids[-1] == ",":
        webappids = webappids[:-1]
    webappid_list = webappids.split(",")

    main(webappid_list,webappids)
