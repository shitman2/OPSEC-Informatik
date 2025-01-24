from PIL import Image

def BinToTxt(binary_message):
    chars = binary_message.split("")
    text = ''.join(chr(int(char, 2)) for char in chars if char)
    return text

def DecImg(image_path):
    cleanImg = Image.open(image_path)
    img = cleanImg.load()
    [w, h] = cleanImg.size

