# source: https://learnopencv.com/depth-perception-using-stereo-camera-python-c/

import numpy as np
import cv2
 
# I have disabled calibration below, do calibration, export and use it here
 
# Reading the mapping values for stereo image rectification
# cv_file = cv2.FileStorage("data/stereo_rectify_maps.xml", cv2.FILE_STORAGE_READ)
# Left_Stereo_Map_x = cv_file.getNode("Left_Stereo_Map_x").mat()
# Left_Stereo_Map_y = cv_file.getNode("Left_Stereo_Map_y").mat()
# Right_Stereo_Map_x = cv_file.getNode("Right_Stereo_Map_x").mat()
# Right_Stereo_Map_y = cv_file.getNode("Right_Stereo_Map_y").mat()
# cv_file.release()
 
def nothing(x):
    pass
 
cv2.namedWindow('disp',cv2.WINDOW_NORMAL)
cv2.resizeWindow('disp',600,600)
 
cv2.createTrackbar('numDisparities','disp',1,17,nothing)
cv2.createTrackbar('p1','disp',1,17,nothing)
cv2.createTrackbar('p2','disp',1,17,nothing)

cv2.createTrackbar('blockSize','disp',5,50,nothing)
cv2.createTrackbar('uniquenessRatio','disp',15,100,nothing)
cv2.createTrackbar('speckleRange','disp',0,100,nothing)
cv2.createTrackbar('speckleWindowSize','disp',3,25,nothing)
cv2.createTrackbar('disp12MaxDiff','disp',5,25,nothing)
cv2.createTrackbar('minDisparity','disp',5,25,nothing)
 
# Creating an object of StereoBM algorithm
stereo = cv2.StereoSGBM_create()
 
while True:
 
  # Capturing and storing left and right camera images
  rleft_img = cv2.imread('./input/left1.jpeg', cv2.IMREAD_COLOR_RGB)
  right_img = cv2.imread('./input/right1.jpeg', cv2.IMREAD_COLOR_RGB)
   
  imgR_gray = cv2.cvtColor(right_img,cv2.COLOR_BGR2GRAY)
  imgL_gray = cv2.cvtColor(rleft_img,cv2.COLOR_BGR2GRAY)

  # Applying stereo image rectification on the left image
  # Left_nice= cv2.remap(imgL_gray,
  #           Left_Stereo_Map_x,
  #           Left_Stereo_Map_y,
  #           cv2.INTER_LANCZOS4,
  #           cv2.BORDER_CONSTANT,
  #           0)

  Left_nice = imgL_gray.copy()
  Right_nice = imgR_gray.copy()    
  # Applying stereo image rectification on the right image
  # Right_nice= cv2.remap(imgR_gray,
  #           Right_Stereo_Map_x,
  #           Right_Stereo_Map_y,
  #           cv2.INTER_LANCZOS4,
  #           cv2.BORDER_CONSTANT,
  #           0)
 
  # Updating the parameters based on the trackbar positions
  numDisparities = cv2.getTrackbarPos('numDisparities','disp')*16
  p1 = cv2.getTrackbarPos('p1','disp')*8*3*5**2
  p2 = cv2.getTrackbarPos('p2','disp')*32*3*5**2
  blockSize = cv2.getTrackbarPos('blockSize','disp')*2 + 5
  uniquenessRatio = cv2.getTrackbarPos('uniquenessRatio','disp')
  speckleRange = cv2.getTrackbarPos('speckleRange','disp')
  speckleWindowSize = cv2.getTrackbarPos('speckleWindowSize','disp')*2
  disp12MaxDiff = cv2.getTrackbarPos('disp12MaxDiff','disp')
  minDisparity = cv2.getTrackbarPos('minDisparity','disp')
    
  # Setting the updated parameters before computing disparity map
  stereo.setNumDisparities(numDisparities)
  stereo.setP1(p1)
  stereo.setP2(p2)
  stereo.setBlockSize(blockSize)
  stereo.setUniquenessRatio(uniquenessRatio)
  stereo.setSpeckleRange(speckleRange)
  stereo.setSpeckleWindowSize(speckleWindowSize)
  stereo.setDisp12MaxDiff(disp12MaxDiff)
  stereo.setMinDisparity(minDisparity)

  # Calculating disparity using the StereoBM algorithm
  disparity = stereo.compute(Left_nice,Right_nice)
  # NOTE: Code returns a 16bit signed single channel image,
  # CV_16S containing a disparity map scaled by 16. Hence it
  # is essential to convert it to CV_32F and scale it down 16 times.

  # Converting to float32
  disparity = disparity.astype(np.float32)

  # Scaling down the disparity values and normalizing them
  disparity = (disparity/16.0 - minDisparity)/numDisparities

  # Displaying the disparity map
  cv2.imshow("disp",disparity)

  # Close window using esc key
  if cv2.waitKey(1) == 27:
    break
   