##https://stackoverflow.com/questions/49280402/python-change-the-rgb-values-of-the-image-and-save-as-a-image

from PIL import *
from PIL import Image

msg = "Hello world"
picture = "Images/LuigiConvert.jpg"



def encryptImage(jpg):
    index = 0
    #Convert msg to ascii and then binary. Simplifies input values for picture så it's easier to decrypt.
    binMsg = ' '.join(format(ord(char), '08b') for char in msg)
    cleanImg = Image.open(jpg)
    img = cleanImg.load()
    print(cleanImg.size)
    [w,h]=cleanImg.size  #width*height
    pictureLen = w * h * 3
    if len(binMsg) > pictureLen:
        raise ValueError("Message is too large for image. Please use a larger image or shorter message")
    print(binMsg)

#   Calculates the needed y values to fit the message
    for y in range(0,len(binMsg) // w + 1):
        x = 0
        #While the x value is under width stay in that line when width is reached change line
        while x < w and index < len(binMsg):
            rTint, gTint, bTint = 0,0,0
            #get the RGB color of the pixel
            [r,g,b]=img[x,y]

            #Lavet tydeligt så man kan se hvad der foregår med pixelsne
            if binMsg[index] == " ":
                rTint = -5
                gTint = -5
                bTint = -5
            if binMsg[index] == "0":
                rTint = 0
                gTint = -5
                bTint = 0
            if binMsg[index] == "1":
                rTint = 0
                gTint = 0
                bTint = -5
            r = r + rTint
            g = g + gTint
            b = b + bTint

            value = (r, g, b)

            cleanImg.putpixel((x, y), value)

            index += 1
            x += 1
    print(index)
    print(len(binMsg))
    cleanImg.save("Images/Luigi2.jpg", quality=100, subsampling=0)
    cleanImg.show()
    print("Done")




encryptImage(picture)
