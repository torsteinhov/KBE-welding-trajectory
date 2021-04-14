from app import app # treat it like a package
from flask import render_template, request, redirect
from datetime import datetime 

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

@app.route("/profile/<username>")
def profile(username):
    print("username: ", username)
    return render_template("public/profile.html")