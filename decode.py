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


    binary_message = ""

    for y in range(h):
        for x in range(w):
            r1, g1, b1 = img1[x,y]
            r2, g2, b2 = img2[x,y]


            if r1 == r2-3 and g1 == g2-3 and b1 == b2-3:
                binary_message += " "

            if r1 == r2 and g1 == g2-3 and b1 == b2:
                binary_message += "0"

            if r1 == r2 and g1 == g2 and b1 == b2-3:
                binary_message += "1"

            #else:
                #break
    print(binary_message)


decimg("Images/LuigiConvert.jpg", "Images/Luigi2.jpg")
