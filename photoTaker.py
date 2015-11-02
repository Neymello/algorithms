import cv2
import time

# Initiate the VideoCapture with the number of the camera
# In our case: /dev/video0 -> camera = 0
camera = cv2.VideoCapture(0)

# Get an image from the camera
# the Read function return a tuple
# First value says with the image was successfully read
# Second value is the image we want
ret,frame = camera.read()

# Lets make sure that the image is good
while ret == False:
	ret,frame = camera.read()

# Save the image into a file
filePath = "./photos/%d.png" % int(time.time())
cv2.imwrite(filePath,frame)

# Realease the camera
del(camera)