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


def get_today_datetime_from_str(time_str):
    time_day = datetime.today()
    return datetime(year=time_day.year,
                    month=time_day.month,
                    day=time_day.day,
                    hour=int(time_str[:2]),
                    minute=int(time_str[2:4]),
                    second=int(time_str[4:]))


def get_tomorrow_datetime_from_str(time_str):
    time_day = datetime.today() + timedelta(days=1)
    return datetime(year=time_day.year,
                    month=time_day.month,
                    day=time_day.day,
                    hour=int(time_str[:2]),
                    minute=int(time_str[2:4]),
                    second=int(time_str[4:]))


def get_next_run_time(scheduled_list):
    time_now = datetime.now()
    time_next = None
    time_key = None
    if len(scheduled_list) == 1:
        first_time = get_today_datetime_from_str(scheduled_list[0])
        if time_now < first_time:
            time_next = first_time
        else:
            time_next = get_tomorrow_datetime_from_str(scheduled_list[0])
        time_key = scheduled_list[0]
    else:
        for i in range(len(scheduled_list) - 1):
            first_time = get_today_datetime_from_str(scheduled_list[i])
            second_time = get_today_datetime_from_str(scheduled_list[i + 1])
            if time_now < first_time:
                time_next = first_time
                time_key = scheduled_list[i]
            elif time_now > first_time and time_now < second_time:
                time_next = second_time
                time_key = scheduled_list[i + 1]
            else:
                time_next = get_tomorrow_datetime_from_str(scheduled_list[0])
                time_key = scheduled_list[0]
    return time_next, time_key


def timed_process(scheduled_dict: dict, time_missfired):
    scheduled_list = sorted(list(scheduled_dict.keys()))
    time_next = None
    retry_time = 0
    missed_retry_time = 0
    time_next, time_key = get_next_run_time(scheduled_list)
    project_list = scheduled_dict.get(time_key)
    print(f'{time_next}----{time_key}')
    print(project_list)
    while True:
        try:
            time_now = datetime.now()
            if time_next is None:
                time_next, time_key = get_next_run_time(scheduled_list)
            time_next_start = time_next
            time_next_end = time_next + timedelta(seconds=time_missfired)

            project_list = scheduled_dict.get(time_key)
            if time_now >= time_next_start and time_now <= time_next_end:
                if project_list is not None:
                    scheduled_run(project_list)
                    logger.info(f"Run At {time_now.strftime('%c')}")
                    time_next = None
                    missed_retry_time = 0
                else:
                    logger.warn(f"Run At {time_now.strftime('%c')} Failed, project list is None")
                    time_next = None
            elif time_now > time_next_end:
                logger.warning("Sync task missed")
                if missed_retry_time < 3:
                    missed_retry_time += 1
                    time_next_start = time_now + timedelta(minutes=30)
                    time_next_end = time_next_start + timedelta(seconds=time_missfired)
                else:
                    logger.error("Sync taks missed retry too many times, exit")
                    raise
            else:
                sleep_seconds = (time_next_start - datetime.now()).total_seconds()
                if sleep_seconds < 10:
                    sleep_seconds = 1
                elif sleep_seconds > 1800:
                    sleep_seconds = 1800
                else:
                    sleep_seconds = sleep_seconds - 2
                logger.info(
                    f"Waiting for next run, {time_next_start.strftime('%c')}, project {','.join(project_list)},  sleeping {sleep_seconds}")
                retry_time = 0
                time.sleep(sleep_seconds)
            time.sleep(0.1)
            retry_time = 0
        except Exception as e:
            logger.error(e)
            if retry_time > 10:
                logger.error("Retry too many times, exit")
                raise Exception("Retry too many times, exit")
            time.sleep(300)
            continue


if __name__ == "__main__":
    scheduled_dict = {
        "060000": ["ring"],
        "040000": ["ocean"]
        # "120000":["vm"]
    }
    time_missfired = 600
    timed_process(scheduled_dict, time_missfired)

