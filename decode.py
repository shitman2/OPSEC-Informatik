from PIL import Image

def bintotxt(binary_message):
    chars = binary_message.split("")
    text = ''.join(chr(int(char, 2)) for char in chars if char)
    return text

def decimg(image_path):
    cleanImg = Image.open(image_path)
    img = cleanImg.load()
    [w, h] = cleanImg.size

    binary_message = ""

    for y in range(h):
        for x in range(w):
            r, g, b = img(x,y)

            if r == 0 and g == 0 and b == 0:
                break

                if r == 0 and g == 0 and b == 255:
                    binary_message += "1"
                elif r == 0 and g == 255 and b == 0:
                    binary_message += "0"
                elif r == 255 and g == 0 and b == 0:
                    binary_message += " "

                    