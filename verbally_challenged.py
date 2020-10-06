"""Use gtts with Python.
 
Create mp3 from text with python, tkinter and gtts

"""
 
# A PROGRAM FROM GIOVANNI GATTO AKA EDUCATIONAL CHANNEL ON YOUTUBE
# AKA PYTHONPROGRAMMI ON TWITTER
# published on http://pythonprogramming.altervista.org
 
from gtts import gTTS
import os
import tkinter as tk
 
root = tk.Tk()
root.geometry("1080x480")
 
# THE ACTION LINKED TO THE EVENT LISTENER
def gorun():
    s = gTTS(text=t.get(), lang=lan.get())
    s.save("Muktak.mp3")
    #filename = mp3.get() + ".mp3"
    os.system('omxplayer Muktak.mp3')
 
# THE FIRST LABEL TELLS YOU WHAT TO DO TO MAKE IT WORK
title = tk.Label(root, text="PRESS ENTER TO HEAR THE TEXT")
title.pack()
title['bg'] = 'yellow'
t = tk.StringVar()
 
# WHERE YOU WRITE THE TEXT
text = tk.Entry(root, textvariable=t, width=90)
text.pack(ipady=10)
t.set("Example of text")
 
# THE LANGUAGE
    # THE LABEL
l2 = tk.Label(root, text="Choose language (default is english=en)")
l2.pack()
    # THE ENTRY WIDGET
lan = tk.StringVar()
language = tk.Entry(root, textvariable=lan)
language.pack()
lan.set("en")
 
# THE NAME OF THE FILE
mp3 = tk.StringVar()
mp3title = tk.Entry(root, textvariable=mp3, width=50)
mp3title.pack()
mp3.set("myfile")
 
# THE EVENT LISTENER
root.bind("<Return>", lambda x: gorun())
 
root.mainloop()
