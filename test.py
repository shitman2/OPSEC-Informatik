from PIL import Image
import numpy as np

def words_to_binary(text):
    return ''.join(format(ord(char),  '08b') for char in text)

def encrypt_img(image_path, message, output_path):
    Img = Image.open(image_path)
    pixel = np.array(Img)



for row in pixel:
    for pixels in row
        for i in range(3):
            if data_index < len(binary_msg):
                pixels[i] = pixels[i] & 