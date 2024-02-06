import json
import requests

#API_ENDPOINT = "http://localhost:5000/generate"
API_ENDPOINT = "https://d9bc-35-229-241-82.ngrok-free.app/generate"

chat = []
chat.append({'role': 'system', 'content': {'type': 'text', 'data': 'You are a helpful assistant'}})
while True:
    user_input = input("User > ")
    chat.append({'role': 'user', 'content': {'type': 'text', 'data': user_input}})
    response = requests.post(url=API_ENDPOINT, json={'chat': chat, 'voice': False}, headers={'Content-type': 'application/json'})
    response = json.loads(response.text)
    chat.append(response)
    print(response)
    if response['content']['type'] == 'text':
        print(f"Assistant > {response['content']['data']}")
    else:
        print("Unknown response")

