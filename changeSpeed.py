# Import everything needed to edit video clips
from moviepy.editor import *

import speech_recognition as sr
import pyttsx3
import os

   
# loading video 
clip = VideoFileClip("Python in 100 Seconds.mp4")
   
# getting only first 5 seconds
clip = clip.subclip(0, 5)
   
# applying speed effect
final = clip.fx( vfx.speedx, 0.5)
  
# showing final clip - works
final.write_videofile("newVideo.mp4")

# Python program to translate
# speech to text and text to speech


#------------------------speech to text-------------------------------
