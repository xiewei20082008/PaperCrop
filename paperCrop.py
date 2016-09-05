import os, sys
from PIL import Image

overlap = 30
kindle2Y = [718,965]
rotateString = ""

mode = sys.argv[1]
file = sys.argv[2]

if mode is 'p':
    step = kindle2Y[1] - overlap
    x = kindle2Y[0]
    y = kindle2Y[1]

elif mode is 'l':
    step = kindle2Y[0] - overlap
    x = kindle2Y[1]
    y = kindle2Y[0]
    rotateString = "-rotate -90"

def getPngHeight(filePath):
    print os.path.dirname(filePath)
    img = Image.open(filePath)
    imageSize = img.size
    return imageSize[1]

def crop(startY,x,y):
    cmd = "magick convert  -crop x"+str(y)+"+0+"+ str(startY)+" " +rotateString+" image.png result"+str(startY/step)+".png"
    print cmd
    os.system(cmd)

height = getPngHeight(file)

for i in range(0,height,step):
    crop(i,x,y)
