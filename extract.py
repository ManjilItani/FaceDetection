# Import everything needed to edit video clips
from moviepy.editor import *
import cv2



def trim(vid):
    # loading video gfg
    clip = VideoFileClip(vid)
    length = clip.duration
    # getting only first 5 seconds
    clip = clip.subclip(length * 0.15, length * 0.30)
    clip.write_videofile("clip.mp4")
# # showing clip
# clip.ipython_display(width = 360)

# clip.write_videofile("clip.mp4")

