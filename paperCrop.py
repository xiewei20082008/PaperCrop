import os, sys
from PIL import Image

overlap = 50
kindle2Y = [718,965]
kobo_forma = [1440,1920]
rotateString = ""

mode = sys.argv[1]
file = sys.argv[2]

resolution = kobo_forma

if mode is 'p':
    step = resolution[1] - overlap
    x = resolution[0]
    y = resolution[1]

elif mode is 'l':
    step = resolution[0] - overlap
    x = resolution[1]
    y = resolution[0]
    rotateString = "-rotate -90"

def getPngHeight(filePath):
    print(os.path.dirname(filePath))
    img = Image.open(filePath)
    imageSize = img.size
    return imageSize[1]

def crop(startY,x,y):
    cmd = "magick convert -quality 100 -crop x"+str(y)+"+0+"+ str(startY)+" " +rotateString+" {} result".format(file)+str(startY//step)+".png"
    print(cmd)
    os.system(cmd)

height = getPngHeight(file)

for i in range(0,height,step):
    crop(i,x,y)
