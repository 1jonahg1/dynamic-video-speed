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
videoSegments = math.ceil(duration / SEGMENT_DURATION)
lastVideoDuration = duration % SEGMENT_DURATION

def splitClips():
  clips = []
  for i in range(videoSegments-1):
    clips.append(clip.subclip((i)*SEGMENT_DURATION, (i+1)*SEGMENT_DURATION))
  clips.append(clip.subclip(duration-lastVideoDuration, duration))
  for index, video in enumerate(clips):
    video.write_videofile("dynamic_test_output/my_video_{}.mp4".format(index))
  return clips

clipList = splitClips()

"""
clip1 = clip.subclip(0, 20)
clip2 = clip.subclip(20, 40)
clip3 = clip.subclip(40, 60)
clip1.write_videofile("dynamic_test_output/my_video_1.mp4")
clip2.write_videofile("dynamic_test_output/my_video_2.mp4")
clip3.write_videofile("dynamic_test_output/my_video_3.mp4")
"""

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
  for index in range(len(clipList)-1):
    words = get_words("my_video_{}".format(index))
    adjustSpeed = WORDS_PER_MINUTE/(words*(60/SEGMENT_DURATION))
    videos.append(Video(speed=adjustSpeed, path="dynamic_test_output/my_video_{}.mp4".format(index)))
  #edit last segment
  words = get_words("my_video_{}".format(index+1))
  adjustSpeed = WORDS_PER_MINUTE/(words*(60/lastVideoDuration))
  videos.append(Video(speed=adjustSpeed, path="dynamic_test_output/my_video_{}.mp4".format(index+1)))
  #update speeds 
  concatenate_videos(videos=videos, output_file=f"dynamic_test_output/final_output_video.mp4")

update_speeds()


"""
#296 in 100 sec -> 178wpm --> I want 300 wpm
words1 = get_words("my_video_1")
words2 = get_words("my_video_2")
words3 = get_words("my_video_3")

videos = [
  Video(speed=300/(words1*3), path="dynamic_test_output/my_video_1.mp4"), # change 3 to 60/video-length
  Video(speed=300/(words2*3), path="dynamic_test_output/my_video_2.mp4"), #change 300 to wanted speed
  Video(speed=300/(words3*3), path="dynamic_test_output/my_video_3.mp4"),
]
"""