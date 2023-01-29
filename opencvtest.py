import numpy as np
import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',0) #1 is colour, 0 is grayscale, -1 is RGBa

#method to show images with openCV
# cv2.imshow('image',img)
# cv2.waitKey(0) #takes key as argument where 0 is any key, and pauses script until pressed
# cv2.destroyAllWindows()

#method to show images with matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([200,300,400],[100,200,300],'c', linewidth=5)# method to plot lines on mpl
plt.show()

cv2.imwrite('watchgray.png',img) #once modified, openCV can save these images.