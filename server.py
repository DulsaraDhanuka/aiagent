import os
from base64 import b64encode
from llama_cpp import Llama
from flask import Flask, abort, request, jsonify

app = Flask(__name__)

llm = Llama(model_path="/kaggle/working/dolphin-2.2.1-mistral-7b.Q6_K.gguf")
audio_sample = '/kaggle/working/sample.wav'

def tts(text):
    os.system(f"""tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \
         --text "{text}" \
         --speaker_wav "{audio_sample}" \
         --language_idx en""")
    enc = None
    with open('output.wav') as f:
        enc = b64encode(f.read())
    return enc

@app.route("/generate", methods=["POST"])
def generate():
    context = ""
    chat = request.json['chat']
    voice = request.json['voice']
    for entry in chat:
        c = f"<|im_start|>{entry['role']}\n"
        if entry['content']['type'] == 'text':
            c += entry['content']['data']
        c += "<|im_end|>\n"
        context += c
    context += "<|im_start|>assistant"
    print(context)
    response = llm(context, max_tokens=8192, stop=["<|im_end|>"], echo=False)
    print(response)
    response = response["choices"][0]["text"].strip()
    if voice:
        return jsonify({'role': 'assistant', 'content': {'type': 'audio', 'data': tts(response), 'text': response}})
    else:
        return jsonify({'role': 'assistant', 'content': {'type': 'text', 'data': response}})

if __name__ == "__main__":
    app.run()

