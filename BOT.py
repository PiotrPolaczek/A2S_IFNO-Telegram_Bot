import a2s
import requests

address = ("90.38.201.141", 27015)

try:
    response = a2s.info(address)

    if response:
        print("sukces")
except TimeoutError:
    TOKEN = "6238535182:AAEUuEZMN-bDf7IKWA2TFG0-G0nzvnNVXQA"
    chat_id = "5861503249"
    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{'6238535182:AAEUuEZMN-bDf7IKWA2TFG0-G0nzvnNVXQA'}/sendMessage?chat_id={'5861503249'}&text={'kupa'}"
    print(requests.get(url).json())  # this sends the message


