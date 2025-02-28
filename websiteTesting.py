import json
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Function for where the data for the image will be saved
app.config['IMAGE_UPLOAD'] = '/website/images'

from werkzeug.utils import secure_filename

@app.route("/home", methods=['POST', 'GET'])
def upload_image():
    if request.method == 'POST':
        print(request.files)
        image = request.files['file'] # Access image (keyword 'file') using files method
        if image.filename == '':
            print("File name is invalid")
            return redirect(request.url)

        # Use werkzeug.utils for secure filename
        filename = secure_filename(image.filename)

        # To access directory of folder to upload file
        basedir = os.path.abspath(os.path.dirname(__file__))

        # Save image in the directory
        image.save(os.path.join(basedir, app.config['IMAGE_UPLOAD'], filename))

        return render_template("index.html", filename=filename)

    return render_template("index.html")

@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('images', filename='/website/images/' + filename), code=301)

app.run(port=5000)

##https://stackoverflow.com/questions/49280402/python-change-the-rgb-values-of-the-image-and-save-as-a-image

from PIL import *
from PIL import Image
from image-view.js import file

msg = "Hello world"
if file == "":
    print("File name is invalid")
else:
    picture = "/website/images/"+file


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
                rTint = -255
                gTint = -255
                bTint = -255
            if binMsg[index] == "0":
                rTint = -255
                gTint = 255
                bTint = -255
            if binMsg[index] == "1":
                rTint = -255
                gTint = -255
                bTint = 255
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
