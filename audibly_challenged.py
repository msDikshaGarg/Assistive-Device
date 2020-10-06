import os
import io
import datetime
import sys
import time
import subprocess
import speech_recognition as sr

from tkinter import *


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/pi/capstonr/capstonr.json"
r= sr.Recognizer()
sample_rate = 48000
root = Tk()
root.geometry("1080x480")
S = Scrollbar(root)
T = Text(root,width=120)
labelfont = ('times', 20, 'bold')
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set, font=labelfont)
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
mic=sr.Microphone(device_index=2)
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
try:
	text = r.recognize_google(audio)
	#print ("you said: " + text)
	T.insert(END, text)
     

except sr.UnknownValueError:
	print(" Speech Recognition could not understand audio")
mainloop()
