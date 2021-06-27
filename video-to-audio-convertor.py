# install moviepy

pip install moviepy

# Code

import moviepy.editor

video = moviepy.editor.VideoFileClip("videosong.mp4") 

# if your video is in same folder where your python file is there then you can give name direct
# else you need to give path of the video file

audio = video.audio
audio.write_audiofile("extractedsong.mp3")

# you can give any name to the converted audio file
