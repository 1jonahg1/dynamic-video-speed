from email.mime import audio
from moviepy.editor import *
import speech_recognition as sr
from adjustPitchSpeed import Video, concatenate_videos
import os
import ffmpeg
import math

SEGMENT_DURATION = 30
#WORDS_PER_MINUTE = 300

# loading video
class DynamicVideoEdit():
    def __init__(self, video_path, input_language, words_per_minute):
        self.clip = VideoFileClip(video_path)
        self.duration = self.clip.duration
        self.video_segments = math.ceil(self.duration / SEGMENT_DURATION)
        self.last_video_duration = self.duration % SEGMENT_DURATION
        self.language = input_language
        self.wpm = words_per_minute

    def splitClips(self):
        clips = []
        for i in range(self.video_segments-1):
            clips.append(self.clip.subclip((i)*SEGMENT_DURATION, (i+1)*SEGMENT_DURATION))
        clips.append(self.clip.subclip(self.duration-self.last_video_duration, self.duration))
        for index, video in enumerate(clips):
            video.write_videofile("dynamic_test_output/my_video_{}.mp4".format(index))
        return clips

    def update_speeds(self, clip_list):
        videos = []
        test_words = []
        for index in range(len(clip_list)-1):
        words = get_words("my_video_{}".format(index))
        test_words.append(words)
        adjust_speed = self.wpm/(words*(60/SEGMENT_DURATION))
        videos.append(Video(speed=adjust_speed, path="dynamic_test_output/my_video_{}.mp4".format(index))) # TODO - change to temp file
        #edit last segment
        words = get_words("my_video_{}".format(index+1))
        adjust_speed = self.wpm/(words*(60/self.last_video_duration))
        videos.append(Video(speed=adjust_speed, path="dynamic_test_output/my_video_{}.mp4".format(index+1)))
        #update speeds 
        concatenate_videos(videos=videos, output_file=f"dynamic_test_output/final_output_video.mp4")
        
        #test
        for i, words in enumerate(test_words):
        print('video {} - words: {}'.format(i,words))

    def get_words(name):
        command2mp3 = "ffmpeg -i dynamic_test_output/{}.mp4 dynamic_test_output/{}.mp3".format(name,name)
        command2wav = "ffmpeg -i dynamic_test_output/{}.mp3 dynamic_test_output/{}.wav".format(name,name)
        os.system(command2mp3)
        os.system(command2wav)
        r = sr.Recognizer()
        with sr.AudioFile("dynamic_test_output/{}.wav".format(name)) as source:
            audio = r.record(source, duration=SEGMENT_DURATION) 
        text = (r.recognize_google(audio, language='he')).split() #language
        print("!!!!Length of text!!!! \n" + str(len(text)))
        return len(text)

    def test_update_audio(wpm, test_video_words = 56, test_video_duration = 19):
        adjust_speed = wpm/(test_video_words*(60/test_video_duration))
        #TODO - adjust the speed of audio (save as temp file?)
