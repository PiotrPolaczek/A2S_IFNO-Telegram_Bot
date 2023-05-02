import a2s
import requests

address = ("SERVERIP", PORT)

try:
    response = a2s.info(address)

    if response:
        print("sukces")
except TimeoutError:
    TOKEN = "TOKEN"
    chat_id = "CHAT_ID"
    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{'TOKEN'}/sendMessage?chat_id={'CHATID'}&text={'MESSENGER'}"
    print(requests.get(url).json())  # this sends the message


