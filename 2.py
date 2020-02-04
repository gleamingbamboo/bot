from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telethon import sync, events
import requests
import json
import hashlib
import time
import re
from virus_total_apis import PublicApi as VirusTotalPublicApi
from telethon import TelegramClient, utils
from telethon.tl.functions.channels import JoinChannelRequest
import webbrowser
import urllib.request
import os

n = 0

api_id = 975469
api_hash = '№№№№№№№№№№№№№№№№№№№№№№№№№№№№№'

client = TelegramClient('anon1', api_id, api_hash)
client.start()

dlgs = client.get_dialogs()

for dlg in dlgs:
    if dlg.title == 'LTC Click Bot':
        tegmo = dlg


class RunChromeTests():
    def testMethod(self):
        caps = {'browserName': 'chrome'}
        driver = webdriver.Remote(command_executor=f'http://localhost:4444/wd/hub', desired_capabilities=caps)
        driver.maximize_window()
        driver.get(url_rec)
        time.sleep(waitin + 10)
        driver.close()
        driver.quit()



    client.send_message('Litecoin_click_bot', "/balance")
    time.sleep(2)
    messages = client.get_messages('Litecoin_click_bot', limit=1)
    for mes in messages:
        str_balance = str(mes.message)
        balance = (str_balance.replace('Available balance: ', '')).replace(' LTC', '')
    client.send_message('Litecoin_click_bot', "/visit")
    if (float(balance)>=0.0004):
        print('Balance:'+balance+' LTC. Time to export money')
    else:
        print('Balance:'+balance+' LTC. more farm!')

while True:
    msgs = client.get_messages(tegmo, limit=1)

    for mes in msgs:
        if re.search(r'\bseconds to get your reward\b', mes.message):
            print("Найдено reward")
            str_response = str(mes.message)
            timer = (str_response.replace('You must stay on the site for', '')).replace('seconds to get your reward.', '')
            waitin = int(timer)
            print("Ждать придется: ", waitin)
            client.send_message('Litecoin_click_bot', "/visit")
            time.sleep(3)
            msgs2 = client.get_messages(tegmo, limit=1)
            for mes2 in msgs2:
                button_data = mes2.reply_markup.rows[1].buttons[1].data
                message_id = mes2.id

                print("Перехожу по ссылке")
                time.sleep(2)
                try:
                    url_rec = messages[0].reply_markup.rows[0].buttons[0].url
                    ch = RunChromeTests()
                    ch.testMethod()
                except:
                    time.sleep(6)
                    fp = urllib.request.urlopen(url_rec)
                    mybytes = fp.read()
                    mystr = mybytes.decode("utf8")
                    fp.close()
                    if re.search(r'\bSwitch to reCAPTCHA\b', mystr):
                        from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

                        resp = client(GetBotCallbackAnswerRequest(
                            'Litecoin_click_bot',
                            message_id,
                            data=button_data
                        ))
                        time.sleep(2)
                        print("КАПЧА!")
                        # os.system("pkill chromium")
                else:
                    time.sleep(waitin)
                    # os.system("pkill chromium")
                    time.sleep(2)

        elif re.search(r'\bSorry\b', mes.message):
            client.send_message('Litecoin_click_bot', "/visit")
            time.sleep(6)
            print("Ads not found")

        else:
            messages = client.get_messages('Litecoin_click_bot')
            time.sleep(5)
            if messages[0].reply_markup != None:
                url_rec = messages[0].reply_markup.rows[0].buttons[0].url
                f = open("per11.txt")
                fd = f.read()
                if fd == url_rec:
                    print("Найдено повторение переменной")
                    msgs2 = client.get_messages(tegmo, limit=1)
                    for mes2 in msgs2:
                        button_data = mes2.reply_markup.rows[1].buttons[1].data
                        message_id = mes2.id
                        from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

                        resp = client(GetBotCallbackAnswerRequest(
                            tegmo,
                            message_id,
                            data=button_data
                        ))
                        time.sleep(2)

                else:
                    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
                    params = {
                        'apikey': '2d090439b3fd029f6b2c28b9f7bc2002e3d0cfd12fe822d358edb3b57e61ad47', 'url': url_rec}
                    response = requests.post(url, data=params)
                    my_file = open('per11.txt', 'w')
                    my_file.write(url_rec)
                    print("Новая запись в файле сделана")
                    time.sleep(16)
                    n = n + 1
                    print("Пройдено циклов: ", n)
            else:
                print("Error, None!!!")