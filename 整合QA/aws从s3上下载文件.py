# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : aws从s3上下载文件.py
@Author : wenjing
@Date : 2022/12/1 11:39
"""
import os
import sys
import traceback
import requests
import json
import socket
import boto3
import time
import threadpool
from datetime import timedelta, datetime
from loguru import logger

tp_size = 80  # 线程池大小
count_interval = 206  # 批处理数量

this_file_path = sys.argv[0]

this_log_file_path = os.path.join('./logs', this_file_path.split('/')[-1].split('.')[0] + '.log')
logger.info(f"this_log_file_path = {this_log_file_path}")

logger.add(this_log_file_path)

ACK = 'xxxxxx'
ACS = 'xxxxxxxxxxxx'

# s3
bucket_name = 'your_bucket_name'  # s3桶名称
remote_dir = 'your_file_path_name'  # 要下载的s3文件夹

s3 = boto3.client('s3', region_name='cn-north-4', aws_access_key_id=ACK, aws_secret_access_key=ACS)

# 文件路径
local_save_path = './'  # s3文件下载到本地临时存储路径


def _get_all_s3_objects(**base_kwargs):
    """
    获取s3_objects列表
    """
    try:
        continuation_token = None
        while True:
            list_kwargs = dict(MaxKeys=1000, **base_kwargs)
            if continuation_token:
                list_kwargs['ContinuationToken'] = continuation_token
            response = s3.list_objects_v2(**list_kwargs)
            yield from response.get('Contents', [])
            if not response.get('IsTruncated'):  # At the end of the list?
                break
            continuation_token = response.get('NextContinuationToken')
    except:
        # send_dingtalk_message(traceback.format_exc())
        logger.error(traceback.format_exc())


def create_assist_date(date_start=None, date_end=None):
    """
    生成指定时间段内的 Date Str List
    :param date_start: 开始时间
    :param date_end: 结束时间
    :return: date_list
    """
    if date_start is None:
        date_start = '2020-01-01'
    if date_end is None:
        date_end = datetime.now().strftime('%Y-%m-%d')

    # 转为日期格式
    date_start = datetime.strptime(date_start, '%Y-%m-%d')
    date_end = datetime.strptime(date_end, '%Y-%m-%d')
    date_list = [date_start.strftime('%Y-%m-%d')]
    while date_start < date_end:
        date_start += timedelta(days=+1)  # 日期叠加一天
        date_list.append(date_start.strftime('%Y-%m-%d'))  # 日期转字符串存入列表

    return date_list


class ZipS3TmallFiles(object):

    def __init__(self):
        self.s3_file_path = ''  # 要下在的s3路径
        self.local_file_path = ''  # s3下载后本地存储路径
        self.local_zip_file_path = ''  # 本地压缩文件存储路径
        self.error_item_count = 0
        self.execute_delete = True

    def _act_download_json_file(self, key_name):
        """从s3下载"""
        logger.info(f"--- key_name = {key_name}")
        file_name = key_name.split('/')[-1]
        content_dir = key_name.replace(file_name, '')
        # logger.info(f"--- content_dir = {content_dir} | file_name = {file_name}")

        resource_local = os.path.join(local_save_path, content_dir)  # 本地存储路径
        # logger.info(f" 本地存储路径 resource_local = {resource_local}")
        if not os.path.exists(resource_local):
            os.makedirs(resource_local)

        local_storage = os.path.join(resource_local, file_name)  # 本地存储路径全路径
        logger.info(f"local_storage = {local_storage}")
        if os.path.exists(local_storage):
            logger.info('Skip Exist File {}'.format(local_storage))
            return
        try:
            with open(local_storage, 'wb') as f:
                s3.download_fileobj(bucket_name, key_name, f)
                f.close()
        except OSError as e:
            self.error_item_count += 1
            logger.error(traceback.format_exc())
            return

    def download_s3_files(self, ):
        # try:
        # 获取s3_objects列表
        s3_objects = _get_all_s3_objects(Bucket=bucket_name, Prefix=remote_dir)
        key_content_list = []
        total_content_size = 0

        # task_pool = threadpool.ThreadPool(tp_size)
        for contents in s3_objects:
            key_value = contents.get('Key', None)
            file_size = contents.get('Size', 0)
            key_content_list.append(key_value)
            total_content_size += file_size

        total_item_count = len(key_content_list)
        # if total_item_count > 0:
        #     key_content_list.pop(0)

        temp_info = 'list Objects, Objects Count: {}, ' \
                    'Total Size Is: {} GB | pid = {} | ppid = {}'.format(
            total_item_count,
            total_content_size / 1024 / 1024 / 1024,
            os.getpid(),
            os.getppid()
        )
        logger.info(temp_info)

        # logger.info(f"key_content_list = {key_content_list}")

        # 单任务
        for index, key_name in enumerate(key_content_list):
            logger.info(f"key_name before = {key_name} | {index + 1}/{len(key_content_list)}")
            # 单
            self._act_download_json_file(key_name)
            logger.info(f"key_name after = {key_name} | {index + 1}/{len(key_content_list)}")

        # 并发
        # for i in range(0, total_item_count, count_interval):
        #     start = i
        #     end = i + count_interval
        #     if end > total_item_count:
        #         end = total_item_count
        #
        #     curr_task_list = key_content_list[start: end]
        #
        #     # 从s3下载
        #     task_pool = threadpool.ThreadPool(tp_size)
        #     requests = threadpool.makeRequests(self._act_download_json_file, curr_task_list)
        #     [task_pool.putRequest(req) for req in requests]
        #     task_pool.wait()

        # except:
        #     logger.error(traceback.format_exc())


def fetch_s3_zip_files():
    """
    下载s3文件
    """
    # 初始化实例
    zip_s3_files = ZipS3TmallFiles()

    # 从s3下载文件
    zip_s3_files.download_s3_files()


def generate_zipped_tasks():
    start_time = time.time()
    fetch_s3_zip_files()

    #  统计信息
    last_messege = f"Sub-process(es) done. " \
                   f"| All Consum Time: {round((time.time() - start_time) / 60, 2)} Min "
    logger.info(last_messege)


if __name__ == '__main__':
    generate_zipped_tasks()
