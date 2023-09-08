import os
from flask import Flask, render_template, request
from models import *
from models import db


app = Flask(__name__) # creating the app

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
 # tells the file where to find the databse
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # turn off autimatic changes "it used in Debuging"

db.init_app(app)

# single / for the home
# just time it differnt in every browser (not same at all users)
@app.route("/")  # adding dirctory for the next exactly function
def index():
    flights = Flight.query.all()
    return render_template("index.html" ,flights = flights )

@app.route("/book" , methods = ['POST'])  
def book():
    cname = request.form.get("custname")
    # try catch
    if cname == "":
        return "ERROR"
    newid = 0
    try :
        newid = int(request.form.get("inserted"))
    except:
        return "ERROR"    
    # does id in flights ?
    iscou = Flight.query.get(newid)
    if iscou is None:
        return "ERROR"
    iscou.add_pass(cname)
    passengers = Passenger.query.all()
    db.session.commit()
    
    return render_template("booked.html" , passes = passengers )
@app.route("/flights")
def preflights():
    flights = Flight.query.all()
    return render_template("flights.html" , flights = flights )


@app.route("/flights/<int:flight_id>" , methods = ['POST','GET'])
def prefi(flight_id):
    ourflight = Flight.query.get(flight_id)
    
    if ourflight is None :
        return "No passengers"
    pass_flights = ourflight.passenger
    return render_template("idflight.html" , flights = pass_flights )
    
