##https://stackoverflow.com/questions/49280402/python-change-the-rgb-values-of-the-image-and-save-as-a-image

from PIL import *

msg = "Hello world"
picture = "Images/LuigiConvert.jpg"





def readPixels(jpg):
    index = 0
    binMsg = ' '.join(format(ord(char), '08b') for char in msg)
    cleanImg=Image.open(jpg)
    img=cleanImg.load()
    print(cleanImg.size)
    [w,h]=cleanImg.size  #width*height
    pictureLen = w * h * 3  # /8????? Vent nvm. Tænkte at vi sammenlignede den ikke binære med billedet. /8 er unødvendig
    if len(binMsg) > pictureLen:
        raise ValueError("Message is too large for image. Please use a larger image or shorter message")
    print(binMsg)

#   Go through a pixel for every character in binMsg
    for y in range(0,len(binMsg) // w + 1):
        for x in range(0,w * (len(binMsg) // w) + len(binMsg) % w):
            tint = 0
            #get the RGB color of the pixel
            [r,g,b]=img[x,y]

            if binMsg[index] == " ":
                tint = 0
            if binMsg[index] == "0":
                tint = -1
            if binMsg[index] == "1":
                tint = -2

            r, g, b= r + tint, g + tint, b + tint
            #g = g + tint
            #b = b + tint

            value = (r, g, b)

            cleanImg.putpixel((x, y), value)

            index += 1
    print(index)
    print(len(binMsg))
    cleanImg.save("Images/Luigi2.jpg")
    cleanImg.show




readPixels(picture)
