#Install Library using command: pip install moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip("Vidoe File Location")
audio = video.audio
audio.write_audiofile("Audio File Location")
