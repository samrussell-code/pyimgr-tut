from PIL import Image
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import time


def threshold(imageArray):
    ''' Reduces the image into black and white by looking at the average RGB values ignoring alpha
        Creates an array of average RGBs for each pixel, which is then meaned to find darkness of image.
        Iterates again through the pixels and compares their mean to the darkness to determine black or white.
        Overwrites each pixel as either black or white, and returns the overwritten array.
    '''
    meansArray = []
    newArray = imageArray
    for row in imageArray:
        for pixel in row:
            avg = mean(pixel[:3])
            meansArray.append(avg)
    darkness = mean(meansArray)
    for row in newArray:
        for pixel in row:
            if mean(pixel[:3])>=darkness:
                pixel[0]=255 #R
                pixel[1]=255 #G
                pixel[2]=255 #B
                pixel[3]=255 #A
            else:
                pixel[0]=0 #R
                pixel[1]=0 #G
                pixel[2]=0 #B
                pixel[3]=255 #A
    return newArray
    
# i = Image.open('images/numbers/y0.5.png')
# iar = np.asarray(i)
# plt.imshow(iar)
# print(iar)
# plt.show()
# represented as a 3d array where each subsidiary array is a column of pixels
# within that row is top to bottom ordered arrays n that contain elements RGBa for their relevant pixel.
i = Image.open('images/numbers/0.1.png')
iar = np.array(i)
i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

iar4t = np.array(i4)
iar4t=threshold(iar4t)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar4)
ax3.imshow(iar3)
ax4.imshow(iar4t)


plt.show()