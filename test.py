from moviepy.editor import *

import speech_recognition as sr

from adjustPitchSpeed import Video, concatenate_videos

# loading video 
clip = VideoFileClip("Python in 100 Seconds.mp4")
   
# getting only first 5 seconds
clip1 = clip.subclip(0, 5)
clip2 = clip.subclip(5, 15)
clip3 = clip.subclip(15, 25) 

clip1.write_videofile("test_output/my_video_1.mp4")
clip2.write_videofile("test_output/my_video_2.mp4")
clip3.write_videofile("test_output/my_video_3.mp4")

videos = [
  Video(speed=1.0, path="test_output/my_video_1.mp4"),
  Video(speed=2.0, path="test_output/my_video_2.mp4"),
  Video(speed=0.5, path="test_output/my_video_3.mp4"),
]

concatenate_videos(videos=videos, output_file=f"test_output/final_output_video.mp4")