# dynamic-video-speed

Dynamic Video Speed is a tool that automatically adjusts the speed of a video to the desired rate specified by the user in words per minute.
This is achieved by dividing the video into segments, adjusting the speed of each segment based on the speaking rate, and reassembling the video. 
For example the tool could be used to watch a lecture at a constant speed, which could be determined by the user's optimal learning speed for watching lectures.  

## Table of contents
* [Libraries](#Libraries)
* [Classes](#Classes)
* [Considerations](#Considerations)
* [Contributions](#Contributions)


# Libraries
* FFmpeg and MoviePy as the video editing tools.
* Google's Speech Recognition API to accurately determine the number of words spoken in each segment.

# Classes
* DynamicVideoEdit.py: The main class that manages the process of dividing the video into segments, adjusting the speeds, and reassembling the video. It also utilizes Google's Speech Recognition API to accurately determine the number of words spoken in each segment.
* AdjustPitchSpeed.py: A class that adjusts the pitch of the video in conjunction with the speed adjustment, ensuring a balanced sound throughout the edited video.
* interface.py: A preliminary user interface built with tkinter, providing a more user-friendly experience when adjusting the speed of a video.

# Considerations in using the tool
While this tool offers a convenient solution for adjusting the speed of a video based on the speaker's rate, it is important to note that the current process can take a significant amount of time, especially due to the time it takes in saving each segment's mp4's seperately before reassembling them. 

# Contributions
Contributions are welcome! If you would like to contribute through code or with ideas for improvements, please open a pull request.
