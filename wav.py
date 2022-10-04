from email.mime import audio
from moviepy.editor import *
import speech_recognition as sr
from adjustPitchSpeed import Video, concatenate_videos
import os
import ffmpeg
import math

command2wav = "ffmpeg -i TestAudio.mp3 TestAudio.wav"
os.system(command2wav)
r = sr.Recognizer()
with sr.AudioFile("TestAudio.wav") as source:
    audio = r.record(source) 
text = (r.recognize_google(audio)).split()
print("!!!!Length of text!!!! \n" + str(len(text)))
