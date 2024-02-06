import json
from base64 import b64decode
import requests
from playsound import playsound

#API_ENDPOINT = "http://localhost:5000/generate"
API_ENDPOINT = "https://5f28-35-229-241-82.ngrok-free.app/generate"

chat = []
chat.append({'role': 'system', 'content': {'type': 'text', 'data': 'You are a helpful assistant'}})
while True:
    user_input = input("User > ")
    chat.append({'role': 'user', 'content': {'type': 'text', 'data': user_input}})
    response = requests.post(url=API_ENDPOINT, json={'chat': chat, 'voice': True}, headers={'Content-type': 'application/json'})
    print(response.text)
    response = json.loads(response.text)
    if response['content']['type'] == 'text':
        print(f"Assistant > {response['content']['data']}")
        chat.append({'role': 'assistant', 'content': {'type': 'text', 'data': response['content']['data']}})
    elif response['content']['type'] == 'audio':
        print(f"Assistant > {response['content']['text']}")
        chat.append({'role': 'assistant', 'content': {'type': 'text', 'data': response['content']['text']}})
        fname = f"{time.time()}.wav"
        with open(fname, 'w+') as f:
            f.write(b64decode(response['content']['data']))
        playsound(fname)
    else:
        print('Unknown data received')
        print(response)

