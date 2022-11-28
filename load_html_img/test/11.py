from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import json
import sys
from pathlib import Path


# from ctypes import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.support.ui import WebDriverWait
# from lxml import html
# import requests
# import pyautogui
# import win32api
# import win32clipboard
# import win32con

def main(json_path):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=service, chrome_options=options)
    browser.maximize_window()
    # SEQUENCE = 'CCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACAGCTCAAACACAAAGTTACCTAAACTATAGAAGGACA'
    with open(json_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
        for html_url in json_data:
            url = html_url['page_url']
            folder_path = "H:/Wenjing/html_folder"
            os.makedirs(folder_path, exist_ok=True)

            # # 写入html文件
            f = open(f"{folder_path}/{html_url['domain'].split('.')[0]}.html", 'wb')
            browser.get(url)
            time.sleep(2)  # 保证浏览器响应成功后再进行下一步操作
            f.write(browser.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
            f.close()

            # # 截图
            folder_path1 = "H:/Wenjing/img_folder"
            os.makedirs(folder_path1, exist_ok=True)
            picture_name1 = f"{folder_path1}/{html_url['domain'].split('.')[0]}.png"
            browser.save_screenshot(picture_name1)
            browser.get(url)
            width = browser.execute_script("return document.documentElement.scrollWidth")
            height = browser.execute_script("return document.documentElement.scrollHeight")
            # width1 = browser.execute_script("return document.body.clientWidth")
            # height1 = browser.execute_script("return document.body.clientHeight")
            browser.set_window_size(width, height)
            time.sleep(1)
            browser.save_screenshot(picture_name1)
            # browser.close()
            # print(width,width1,height,height1)

            # # 12
            # # seq_query_field = driver.find_element_by_id("seq")
            # # seq_query_field.send_keys(SEQUENCE)
            # # blast_button = driver.find_element_by_id("b1")
            # # blast_button.click()
            # browser.get(url)
            # time.sleep(5)
            # # 等待结果加载
            # # WebDriverWait(browser, 60).until(visibility_of_element_located((By.ID, 'grView')))
            # # 打开"另存为"来保存html和资源文件
            # pyautogui.hotkey('ctrl', 's')
            # time.sleep(1)
            # pyautogui.typewrite(SEQUENCE + '.html')
            # pyautogui.hotkey('enter')

            # # 112
            # browser.get(url)
            # # seq_query_field = browser.find_element_by_id("seq")
            # # seq_query_field.send_keys(SEQUENCE)
            # # blast_button = browser.find_element_by_id("b1")
            # # blast_button.click()

            # # # write the page content
            # f = open(f"{folder_path}/{html_url['domain'].split('.')[0]}.html", 'wb')
            # time.sleep(2)  # 保证浏览器响应成功后再进行下一步操作
            # f.write(browser.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
            # f.close()

            # # download the referenced files to the same path as in the html
            # sess = requests.Session()
            # sess.get(url)            # sets cookies

            # # parse html
            # content = browser.page_source
            # h = html.fromstring(content)
            # # get css/js files loaded in the head
            # for hr in h.xpath('head//@href'):
            #     if not hr.startswith('http'):
            #         local_path = 'H:/Wenjing/html_folder' + hr.replace('//','/')
            #         local_path = local_path.replace('?','')
            #         hr = base + hr.replace('//','/')
            #     res = sess.get(hr)
            #     if not os.path.exists(os.path.dirname(local_path)):
            #         os.makedirs(os.path.dirname(local_path))
            #     with open(local_path, 'wb') as fp:
            #         fp.write(res.content)

            # # get image/js files from the body.  skip anything loaded from outside sources
            # for src in h.xpath('//@src'):
            #     if not src or src.startswith('http'):
            #         continue
            #     local_path = f'{folder_path}/' + src
            #     print(local_path)
            #     src = url + src
            #     res = sess.get(hr)
            #     if not os.path.exists(os.path.dirname(local_path)):
            #         os.makedirs(os.path.dirname(local_path))
            #     with open(local_path, 'wb') as fp:
            #         fp.write(res.content)

            # 1.mthml
            # browser.get(url)
            # data = browser.execute_cdp_cmd('Page.captureSnapshot', {}).get('data')
            # with open(f"{folder_path}/{html_url['domain'].split('.')[0]}.mhtml", 'w+',newline='') as f:
            #     f.write(data)
            # 2.
            # browser.get(url)
            # time.sleep(2)
            # # #获取页面title作为文件名
            # # title=browser.title
            # # print(title)
            # #设置当前路径为：当前项目的+文件名
            # path=f"{folder_path}/{html_url['domain'].split('.')[0]}.html"
            # #将路径复制到剪切板
            # win32clipboard.OpenClipboard()
            # win32clipboard.EmptyClipboard()
            # win32clipboard.SetClipboardText(path)
            # win32clipboard.CloseClipboard()
            # #按下Ctrl+s
            # win32api.keybd_event(0x11,0,0,0)
            # win32api.keybd_event(0x53,0,0,0)
            # win32api.keybd_event(0x53,0,win32con.KEYEVENTF_KEYUP,0)
            # win32api.keybd_event(0x11,0,win32con.KEYEVENTF_KEYUP,0)
            # time.sleep(3)
            # #鼠标定位输入框并点击
            # windll.user32.SetCursorPos(700,510)
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
            # time.sleep(3)
            # # #按下回车
            # win32api.keybd_event(0x0D,0,0,0)
            # win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)
            # time.sleep(1)
            # win32api.keybd_event(0x0D,0,0,0)
            # win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)
            # time.sleep(10)#下载需要时间


if __name__ == '__main__':
    json_path = Path(f"{sys.argv[1]}")
    # json_path = r'H:/Wenjing/Product_batch_3_221121.json'
    main(json_path)