from app import app # treat it like a package
from flask import render_template, request, redirect
from datetime import datetime 
import os
import os.path
from os import path
from werkzeug.utils import secure_filename
from ImgWeldLinesGenerator.ImgGenerator import runImgGenerator
from PIL import Image
from datetime import date


#torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory"
#aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory"
processEngineer_path = <YOUR_PATH_HERE>
yourLocation = processEngineer_path

@app.route("/") # home page
def index():
    
    return render_template("public/index.html")

@app.route("/about") # about page
def about():
    return render_template("public/about.html")


@app.route("/imgOrder", methods=["GET", "POST"]) # imgOrder page
def imgOrder():

    if request.method == "POST":  # handels input form customer

        return redirect(request.url)
    return render_template("public/imgOrder.html")

# some configurations for the website
app.config["IMAGE_UPLOADS"] = yourLocation + "\\imgFromCustomer"
app.config["SAVED_WELDINGLINES_IMAGES"] = yourLocation + "\\app\static\img"
app.config["PRT_FILES_UPLOAD"] = yourLocation + "\\prt"
app.config["ALLOWED_IMAGE_EXTENTIONS"] = ["PNG", "JPG", "JPEG", "GIF", "PRT"]
app.config["ALLOWED_CAD_EXTENTIONS"] = ["PRT"]
app.config["MAX_IMAGE_FILESIZE"] = 20000000

# checks if the filetype is allowed by us
def allowed_image(filename):
  if not "." in filename:
    return False

  ext = filename.rsplit(".", 1)[1] # ser hva som skjer etter punktum
  if ext.upper() in app.config["ALLOWED_IMAGE_EXTENTIONS"]:
    return True
  else:
    return False

# checks if the filetype is allowed by us
def allowed_cad(filename):
  if not "." in filename:
    return False

  ext = filename.rsplit(".", 1)[1] # ser hva som skjer etter punktum
  if ext.upper() in app.config["ALLOWED_CAD_EXTENTIONS"]:
    return True
  else:
    return False

# checks if we allow the filetype
def allowed_image_filesize(filesize):

  if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
    return True
  else:
    return False

def saveFileNewName(oldName, newName): #save the file again with correct name
    img= Image.open(oldName)
    img = img.save(newName)

def updatLogFile(name,email,company,infile,outfile): #logfile for the system
    #ta inn navn og sånn
    #lagre til fila
    #lagre dato
    
    nowObj = datetime.now()
    nowStr = nowObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("Type: ", type(nowStr))

    logLine = str(nowStr) + ", " + name + ", " + email +", "+ company + ", " + infile +", "+outfile + ".\n"
    logfilePath = yourLocation + "\\LogOrder.txt" 
    if path.exists(logfilePath):
        f = open(logfilePath, "a")
    else:
        f = open(logfilePath, "w")
    
    f.write(logLine)
    f.close()
    
@app.route("/imgResult", methods=["GET", "POST"]) #the feedback after ordering imge-welding lines
def imgResult():
    print("Inside imgResult")
    #if request.method == "POST":
    print("request.files: ", request.files)


    if request.files: # if there has been uploaded a file
        
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

            # getting the data from the customer into variables we could handle --> string parsing
            name =request.form["name"]
            email = request.form["email"]
            company = request.form["Company"]

            print(name, email, company)
            details = name.replace(" ", "_") + company.replace(" ", "_")

            if path.exists(app.config["SAVED_WELDINGLINES_IMAGES"] +"\\result.jpg"): # this is suppose to dele the result file. 
                print("Denne filen finnes")
                os.remove(app.config["SAVED_WELDINGLINES_IMAGES"] +"\\result.jpg")
            
            # checks if it is a cad-file
            if filename.split(".")[1] == "prt":
                image.save(os.path.join(app.config["PRT_FILES_UPLOAD"], details+filename))
                print("PRT-file from customer saved.")
                updatLogFile(name,email, company,details+filename,"None")

                return render_template("public/prtResult.html") # redirect the customer to this page

            # assuming it is a image
            else:
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                print("Image from customer saved.") 

                
                if not ".jpg" in filename: #convert the file to jpg
                    savename = filename.split(".")[0]
                    savename= savename+".jpg"
                else:
                    savename=filename

                if path.exists(app.config["SAVED_WELDINGLINES_IMAGES"] +"\\result.jpg"): # delets the result file if it exists
                    print("Denne filen finnes")
                    os.remove(app.config["SAVED_WELDINGLINES_IMAGES"] +"\\result.jpg")

                # Here comes the call on the welding generator for images
                runImgGenerator(app.config["IMAGE_UPLOADS"]+"\\"+filename, app.config["SAVED_WELDINGLINES_IMAGES"] +"\\result.jpg" ) # saving the generated image as "result.jpg"
                print("Image grenerator is done.")
                saveFileNewName(app.config["SAVED_WELDINGLINES_IMAGES"] +"\\result.jpg", app.config["SAVED_WELDINGLINES_IMAGES"] +"\\"+savename)
                
                #updating the logfile
                updatLogFile(name,email,company,filename,savename)

        return redirect(request.url)
    
    return render_template("public/imgResult.html")

