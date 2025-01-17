##https://stackoverflow.com/questions/49280402/python-change-the-rgb-values-of-the-image-and-save-as-a-image

from PIL import *


def readPixels(jpg):
  im=Image.open(jpg)
  img=im.load()
  print(im.size)
  [xs,ys]=im.size  #width*height

# Examine every pixel in im
  for x in range(0,xs):
     for y in range(0,ys):
        #get the RGB color of the pixel
        [r,g,b]=img[x,y]

readPixels()