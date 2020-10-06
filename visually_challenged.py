import os
import io
import datetime
import sys
import time
import subprocess
from google.cloud import vision
from gtts import gTTS
# read the absolute path
# call the .sh to capture the image
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/pi/capstonr/capstonr.json"
client = vision.ImageAnnotatorClient()
os.system('fswebcam -r 1280x720 --no-banner /home/pi/capstonr/test.jpg')
path = '/home/pi/capstonr/test.jpg'
with io.open(path, 'rb') as image_file:
    content = image_file.read()
image = vision.types.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations
if len(texts) > 0:
        text = texts[0].description
else:
    text = ''
print(text)
language = 'en'

myobj = gTTS(text=text , lang=language, slow=False)
myobj.save("spoken.mp3")
# os.system("mpg321 spoken.mp3")
# from pygame import mixer # Load the required library

# mixer.init()
# mixer.music.load('spoken.mp3')
# mixer.music.play()
os.system('omxplayer spoken.mp3')
