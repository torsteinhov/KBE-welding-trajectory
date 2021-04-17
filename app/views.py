from app import app # treat it like a package
from flask import render_template, request, redirect
from datetime import datetime 
import os
from werkzeug.utils import secure_filename
from ImgWeldLinesGenerator.ImgGenerator import runImgGenerator

aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory"
yourLocation = aashild_path

@app.template_filter("clean_date") #name of custom filter
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():

    
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    my_name ="Aashild"
    age = 23
    langs =["python", "C++", "Matlab", "html"]

    friends = {
        "Anne": 23,
        "Sarah": 26,
        "Anne Sofie": 22
    }

    colours = ("Red", "Green")

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        def pull(self):
            return f"Pullin repo {self.name}"
        def clone(self):
            return f"Cloning into {self.url}"
    my_remote = GitRemote(name= "Welding", description= "project", url = "nrk.no")
    
    def repeat(x, qty):
        return x*qty

    date = datetime.utcnow()
    my_html ="<h1>THIS IS SOM HTML.</h1>"
    sus = "<script>alert('you got hacked')</script>"

    return render_template(
        "public/jinja.html", my_name = my_name, age = age,
        langs = langs, friends = friends, colours = colours,
        cool = cool, GitRemote = GitRemote, repeat = repeat,
        my_remote = my_remote, date = date, my_html = my_html,
        sus = sus ) #parse it

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST": 
        req = request.form
        print("req: ", req)

        username =req["username"]
        email = req.get("email")
        password = request.form["password"]

        print(username, email, password)

        return redirect(request.url)

    return render_template("public/sign_up.html")

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}

@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html", username=username, user=user)

@app.route("/prtOrder",  methods=["GET", "POST"]) #prtOrder
def prtOrder():
    if request.method == "POST":
        return redirect(request.url)
    return render_template("public/prtOrder.html")

@app.route("/imgOrder", methods=["GET", "POST"]) #imgOrder
def imgOrder():

    if request.method == "POST": 

        return redirect(request.url)
    return render_template("public/imgOrder.html")

app.config["IMAGE_UPLOADS"] = yourLocation + "\\imgFromCustomer"
app.config["SAVED_WELDINGLINES_IMAGES"] = yourLocation + "\\app\static\img"
app.config["ALLOWED_IMAGE_EXTENTIONS"] = ["PNG", "JPG", "JPEG", "GIF", "PRT"]
app.config["MAX_IMAGE_FILESIZE"] = 20000000#0.5 * 1024 *1024 #ET LITE BILDE

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


@app.route("/imgResult", methods=["GET", "POST"]) #the feedback after ordering imge-welding lines
def imgResult():
    print("Inside imgResult")
    #if request.method == "POST":
    print("request.files: ", request.files)
    if request.files:

        print(request.cookies)
        if not allowed_image_filesize(request.cookies["filesize"]): #sjekker filstørrelsen
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
            img_path = image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            print("image path om maze form customer: ", img_path)
            print("Image saved") 
            # Here comes the call on the welding generator for images
            if ""
            runImgGenerator(app.config["IMAGE_UPLOADS"]+"\\"+filename, app.config["SAVED_WELDINGLINES_IMAGES"] +"\\"+filename )
            print("Image grenerator is done.")

        #image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        print("Image saved") # to get some response

        return redirect(request.url)
    
    return render_template("public/imgResult.html")

@app.route("/prtResult", methods=["GET", "POST"])
def prtRessult():
    if request.method == "POST": 

        return redirect(request.url)
    return render_template("public/prtResult.html")




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
