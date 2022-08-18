import os
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
MY_VID_FILE = os.path.join(BASE_DIR, "inputs") # create input folder inside BASE DIR
THUMBNAIL_PATH = os.path.join(BASE_DIR, "output") # same
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from moviepy.editor import * # NOTES:- PLEASE install this moviepy module
# pip install moviepy

from PIL import Image

video_file = os.path.join(MY_VID_FILE, 'input.mov')
thumnail_dir = os.path.join(THUMBNAIL_PATH, 'thumbnail')

os.makedirs(thumnail_dir, exist_ok=True)

clips = VideoFileClip(video_file)
frames = clips.reader.fps #frame per second
duration = clips.duration # seconds

max_duration = int(duration)+1

i = max_duration//2  # Get the thumbnail in middle of the video

# You can get more thumbnails with using for loop

frame = clips.get_frame(i)

new_img_file = os.path.join(thumnail_dir, f"{i}.jpg")

new_img = Image.fromarray(frame)
new_img.save(new_img_file)