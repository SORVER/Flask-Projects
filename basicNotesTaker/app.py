from flask import Flask , render_template , request ,session
from flask_session import Session
# we may use pip3 install flask-session
app = Flask(__name__) # creating the app

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# single / for the home
# just time it differnt in every browser (not same at all users)
@app.route("/", methods = ["GET", "POST"])  # adding dirctory for the next exactly function
def index():
    if session.get("master") is None:  # is and not == , session.get("master")  not session["master"] 
        session["master"] = []
    if request.method == "POST":
        note = request.form.get("anote")
        session["master"].append(note)
    return render_template("index.html", notes =  session["master"])

