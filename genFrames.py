import cv2
from numpy import half
from extract import trim

trim('input2.mp4')
vidcap = cv2.VideoCapture('clip.mp4')
# Get the total number of frames
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
# half_point = length//2 # Approximately half if number of frames are odd
# print(half_point)
# Set the reader to the given frame number (half_point)
success,image = vidcap.read()
count = 0
# while success and count < half_point:
  # if count < half_point/2:
  #   count += 1
  #   continue

while success:
  cv2.imwrite("./shots/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1