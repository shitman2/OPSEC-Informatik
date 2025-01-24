from PIL import Image
import numpy as np

def TxtBin(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encodeimage(image_path, message, output_path):
    img = Image.open(image_path)
    pixels = np.array(img)

    binary_message = TxtBin(message) + '1111111111111110'  # End marker
    data_index = 0

    for row in pixels:
        for pixel in row:
            for i in range(3):  # Iterate over RGB channels
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
                else:
                    break

    encoded_img = Image.fromarray(pixels)
    encoded_img.save(output_path)
    print("Message encoded successfully!")


encodeimage('u put ur png file name here', 'the hidden msgs', 'and the name of the new pic it will make')