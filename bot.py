import requests
import time
jokes = [""" Put your message here"""]

file = 'Link to picture'
api_url = 'https://api.telegram.org/bot[BOT_TOKEN]/'

chats = ['CHANNELS_iDS']
def send_photo(chat_id, file_opened, jk):
    method = "sendPhoto"
    params = {'chat_id': chat_id, 'photo': file_opened, 'caption': jk }
    
    resp = requests.get(api_url + method, params)
    return resp



def send_text(chat_id, text):
    method = "sendMessage"
    params = {'chat_id': chat_id, 'text': text}
    resp = requests.get(api_url + method, params)
    return resp

for chat in chats:
    for joke in jokes:
        
        send_photo(chat, file, joke )
        time.sleep(10)
        print('SENT!!!')

    
