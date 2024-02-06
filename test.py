import os
from base64 import b64encode

with open('tts_output.wav', 'rb') as f:
    enc = b64encode(f.read())

print(enc)

