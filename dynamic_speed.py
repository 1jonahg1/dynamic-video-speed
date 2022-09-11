from moviepy.editor import *
import speech_recognition as sr
from adjustPitchSpeed import Video, concatenate_videos
import os
import ffmpeg
import subprocess
import math

SEGMENT_DURATION = 30
WORDS_PER_MINUTE = 300

# loading video
clip = VideoFileClip("Python.mp4")
duration = clip.duration
video_segments = math.ceil(duration / SEGMENT_DURATION)
last_video_duration = duration % SEGMENT_DURATION

def splitClips():
  clips = []
  for i in range(video_segments-1):
    clips.append(clip.subclip((i)*SEGMENT_DURATION, (i+1)*SEGMENT_DURATION))
  clips.append(clip.subclip(duration-last_video_duration, duration))
  for index, video in enumerate(clips):
    video.write_videofile("dynamic_test_output/my_video_{}.mp4".format(index))
  return clips

clip_list = splitClips()


def get_words(name):
    command2mp3 = "ffmpeg -i dynamic_test_output/{}.mp4 dynamic_test_output/{}.mp3".format(name,name)
    command2wav = "ffmpeg -i dynamic_test_output/{}.mp3 dynamic_test_output/{}.wav".format(name,name)
    os.system(command2mp3)
    os.system(command2wav)
    r = sr.Recognizer()
    with sr.AudioFile("dynamic_test_output/{}.wav".format(name)) as source:
        audio = r.record(source, duration=20) 
    text = (r.recognize_google(audio)).split()
    print("!!!!Length of text!!!! \n" + str(len(text)))
    return len(text)
  
def update_speeds():
  videos = []
  for index in range(len(clip_list)-1):
    words = get_words("my_video_{}".format(index))
    adjust_speed = WORDS_PER_MINUTE/(words*(60/SEGMENT_DURATION))
    videos.append(Video(speed=adjust_speed, path="dynamic_test_output/my_video_{}.mp4".format(index)))
  #edit last segment
  words = get_words("my_video_{}".format(index+1))
  adjust_speed = WORDS_PER_MINUTE/(words*(60/last_video_duration))
  videos.append(Video(speed=adjust_speed, path="dynamic_test_output/my_video_{}.mp4".format(index+1)))
  #update speeds 
  concatenate_videos(videos=videos, output_file=f"dynamic_test_output/final_output_video.mp4")

update_speeds()

