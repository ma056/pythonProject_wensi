
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
from selenium.webdriver.common.action_chains import ActionChains
import win32api
import win32clipboard
import win32con
import win32gui
from selenium.webdriver.common.keys import Keys
pyautogui.FAILSAFE = False
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(service=service, chrome_options=options)
browser.maximize_window()

browser.get('https://defenseinnovation.com/products/universal-hoslter-glock-s-w-sig-sauer-walther-ruger-1911-and-others-left-right-hand')

# save_me = ActionChains(browser).key_down(Keys.CONTROL).key_down('s').key_up(Keys.CONTROL).key_up('s')

# save_me.perform()
# file_object = open("H:/Wenjing/html_folder/aa.html", "wb")
# html = browser.page_source
# file_object.write(html.encode('utf-8'))
# file_object.close()
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# pyautogui.typewrite('H:/Wenjing/html_folder/b.htm')
# time.sleep(1)
# pyautogui.hotkey('enter')
win32api.keybd_event(17, 0, 0, 0)  # 按下ctrl
win32api.keybd_event(83, 0, 0, 0)  # 按下s
win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放s
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放ctrl
hd = win32gui.FindWindow(u"#32770", u"H:/Wenjing/html_folder/a.html")
win32gui.SetForegroundWindow(hd)
time.sleep(0.2)

win32api.keybd_event(13, 0, 0, 0)  # 按下enter
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放enter