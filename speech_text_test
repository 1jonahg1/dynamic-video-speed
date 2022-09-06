import os
import speech_recognition as sr
import ffmpeg

#Converting .mp4 to .mp3
command2mp3 = "ffmpeg -i Python.mp4 speech_to_text_test_output/Python.mp3"

#Converting .mp3 to .wav
command2wav = "ffmpeg -i speech_to_text_test_output/Python.mp3 speech_to_text_test_output/Python.wav"

#Execution of Video conversion commands using os Library:
os.system(command2mp3)
os.system(command2wav)

#Loading and processing the .wav file
r = sr.Recognizer()
with sr.AudioFile("speech_to_text_test_output/Python.wav") as source:
     audio = r.record(source, duration=100) 
print(r.recognize_google(audio))