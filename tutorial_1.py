from flask import Flask, redirect, url_for


app = Flask(__name__)       #instansiation of the page 


@app.route("/")                                         """"********"""
def home():                                                    """ *****"""
    return "Hello! this is Flask<h1>HELLO Flask!<h1>"         """  main page """
@app.route("/<name>")                                           
def user(name):
    return f"Hello, {name}!"  

@app.route("/admin")
def admin():        #only authorized  accounts
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run()
