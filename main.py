##https://stackoverflow.com/questions/49280402/python-change-the-rgb-values-of-the-image-and-save-as-a-image

from PIL import *

msg = "amogus"
picture = "Images/LuigiConvert.jpg"

binMsg = ' '.join(format(ord(char), '08b') for char in msg)
pictureLen = w * h * 3 #/8?????
if len(binMsg > pictureLen):
    raise ValueError("Messge is too large for image. Please use a larger image or shorter message")
print(binMsg)

def readPixels(jpg):
    im=Image.open(jpg)
    img=im.load()
    print(im.size)
    [w,h]=im.size  #width*height

#   Examine every pixel in im
    for x in range(0,w):
        for y in range(0,h):
            #get the RGB color of the pixel
            [r,g,b]=img[x,y]


readPixels(picture)
