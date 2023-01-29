from PIL import Image
from statistics import mean
from collections import Counter
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

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        #print eachNum
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    inQuestion = str(iarl)
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print(str(e))
                
    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]



    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()

# i = Image.open('images/numbers/y0.5.png')
# iar = np.asarray(i)
# plt.imshow(iar)
# print(iar)
# plt.show()
# represented as a 3d array where each subsidiary array is a column of pixels
# within that row is top to bottom ordered arrays n that contain elements RGBa for their relevant pixel.

createExamples()

whatNumIsThis('images/test.png')

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