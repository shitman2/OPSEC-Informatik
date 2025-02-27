from PIL import Image

def bintotxt(binary_message):
    chars = binary_message.split("")
    text = ''.join(chr(int(char, 2)) for char in chars if char)
    return text

def decimg(clean_image_path, dirty_image_path):
    cleanImg = Image.open(clean_image_path)
    img1 = cleanImg.load()
    [w, h] = cleanImg.size

    dirtyImg = Image.open(dirty_image_path)
    img2 = dirtyImg.load()

    tempBinMsg = ""
    binary_message = ""

    for y in range(h):
        for x in range(w):

            r1, g1, b1 = img1[x,y]
            r2, g2, b2 = img2[x,y]

    ½½
            if (r1 == r2-5 or r1 == r2-4 or r1 == r2-6) and (g1 == g2-5 or g1 == g2-4 or g1 == g2-6) and (b1 == b2-5 or b1 == b2-4 or b1 == b2-6):
                tempBinMsg = "".join([binary_message, " "])

            if (r1 == r2 or r1 == r2+1 or r1 == r2-1) and (g1 == g2-5 or g1 == g2-4 or g1 == g2-6) and (b1 == b2 or b1 == b2+1 or b1 == b2-1):
                tempBinMsg = "".join([binary_message, "0"])

            if (r1 == r2 or r1 == r2+1 or r1 == r2-1) and (g1 == g2 or g1 == g2+1 or g1 == g2-1) and (b1 == b2-5 or b1 == b2-4 or b1 == b2-6):
                tempBinMsg = "".join([binary_message, "1"])

            #else:
                #break

            binary_message = tempBinMsg
    print(binary_message)


decimg("Images/LuigiConvert.jpg", "Images/Luigi2.jpg")
