##https://stackoverflow.com/questions/49280402/python-change-the-rgb-values-of-the-image-and-save-as-a-image

from PIL import *

msg = "Hello world"
picture = "Images/LuigiConvert.jpg"





def readPixels(jpg):
    index = 0
    binMsg = ' '.join(format(ord(char), '08b') for char in msg)
    im=Image.open(jpg)
    img=im.load()
    print(im.size)
    [w,h]=im.size  #width*height
    pictureLen = w * h * 3  # /8?????
    if len(binMsg) > pictureLen:
        raise ValueError("Message is too large for image. Please use a larger image or shorter message")
    print(binMsg)

#   Go through every pixel
    for y in range(0,len(binMsg) // w + 1):
        for x in range(0,w * (len(binMsg) // w) + len(binMsg) % w):
            #get the RGB color of the pixel
            [r,g,b]=img[x,y]
            index += 1
    print(index)
    print(len(binMsg))

#len // width
#    len % width




readPixels(picture)
