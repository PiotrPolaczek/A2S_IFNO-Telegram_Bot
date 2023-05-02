import time
import requests
import a2s

address = ("IP", PORT)

while True:
    try:
        response = a2s.info(address)

        if response:
            print("MESSENGER")
    except TimeoutError:
        TOKEN = "TOKEN"
        chat_id = "CHATID"
        message = "hello from your telegram bot"
        url = f"https://api.telegram.org/bot{'TOKEN'}/sendMessage?chat_id={'CHAT_ID'}&text={'MESSENGER'}"
        print(requests.get(url).json())  # this sends the message

    time.sleep(60)


