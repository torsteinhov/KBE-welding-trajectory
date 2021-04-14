import numpy as np
''' #Test av å legge til enere rundt en matrise
matrise = np.array([[1,2,3],
                    [1,2,3],
                    [1,2,3],
                    [1,2,3]])

hoyde = len(matrise)
print("hoyde: ", hoyde)

hoydeVec = np.full(
  shape=hoyde,
  fill_value=1,
  dtype=np.int
).reshape(4,1)
print("hoydeVec: ", hoydeVec)

hoydeVec2 = np.full(
  shape=hoyde+1,
  fill_value=1,
  dtype=np.int
)
print("hoydeVec: ", hoydeVec2)

newImg = np.block([[hoydeVec2],[hoydeVec, matrise, hoydeVec], [hoydeVec2]])
print("newIMG: \n",newImg)
'''

# Flask
# https://www.youtube.com/watch?v=6WruncSoCdI
from app import app
from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime
import os
from werkzeug.utils import secure_filename # for å sjekke om det er et farlig filnavn

app.config["IMAGE_UPLOADS"] = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\HTML\\customerIMG"
app.config["ALLOWED_IMAGE_EXTENTIONS"] = ["PNG", "JPG", "JPEG", "GIF", "PRT"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 *1024 #ET LITE BILDE

def allowed_image(filename):
  if not "." in filename:
    return False

  ext = filename.rsplit(".", 1)[1] # ser hva som skjer etter punktum
  if ext.upper() in app.config["ALLOWED_IMAGE_EXTENTIONS"]:
    return True
  else:
    return False

def allowed_image_filesize(filesize):

  if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
    return True
  else:
    return False


@app.route("/upload-image", methods = ["GET", "POST"])
def upload_image():

  if request.method == "POST":

    if request.files:

      print(request.cookies)
      if not allowed_image_filesize(request.cookies): #sjekker filstørrelsen
        print("File exeeded maximum size")
        return redirect(request.url)

      image = request.files["image"] #store the file in this variable
      #print(image)

      # sikkerhetssjekk:
      if image.filename == "":
        print("Image must have a filename")
        return redirect(request.url)
      
      if not allowed_image(image.filename):
        print("That image extention is not allowed")
        return redirect(request.url) 

      else:
        filename = secure_filename(image.filename) # gi et nytt filnavn
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

      #image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
      print("Image saved") # to get some response

      return redirect(request.url)


  return render_template("public/upload_image.html")