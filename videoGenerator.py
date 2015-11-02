import numpy
from PIL import Image
import cv2
import os

# Define the size of the video
# Must be the same size of the photos
width,height = (640, 480)

# Define the codec
fourcc = cv2.cv.CV_FOURCC('P','I','M','1')
# Create the video pointer
# Params  (file_name,code,frames_per_second,size)
video = cv2.VideoWriter("timelapse.avi",fourcc,20,(width,height))

# List all photos
for i in os.listdir("photos"):
	# Open the file
	im1 = Image.open("photos/"+i)
	# Convert to NumPY array
	frame = numpy.array(im1)

	# Add into the video
	video.write(frame)

# Release the video
video.release()