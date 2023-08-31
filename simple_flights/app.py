import os
from flask import Flask , render_template , request

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

# we may use pip3 install flask-session
app = Flask(__name__) # creating the app

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind= engine))



# single / for the home
# just time it differnt in every browser (not same at all users)
@app.route("/")  # adding dirctory for the next exactly function
def index():
    flights = db.execute(text("SELECT * FROM flights;")).fetchall()
    return render_template("index.html" ,flights = flights )

@app.route("/book" , methods = ['POST'])  # adding dirctory for the next exactly function
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
    iscou = db.execute(text("SELECT * FROM flights WHERE id = :iid ;"), {'iid' : str(newid) }).fetchall()
    if len(iscou) == 0:
        return "ERROR"
    db.execute(text("INSERT INTO passengers (name , flight_id) VALUES (:a , :b)"), {'a' : cname, 'b' :newid})
    passengers = db.execute(text("SELECT * FROM passengers;")).fetchall()
    db.commit()
    
    return render_template("booked.html" , passes = passengers )
@app.route("/flights")
def preflights():
    flights = db.execute(text("SELECT * FROM flights;")).fetchall()
    return render_template("flights.html" , flights = flights )


@app.route("/flights/<int:flight_id>" , methods = ['POST','GET'])
def prefi(flight_id):
    pass_flights = db.execute( text("SELECT * FROM passengers WHERE flight_id = :d"), {'d' : flight_id} ).fetchall()
    if len(pass_flights) != 0 :
        return render_template("idflight.html" , flights = pass_flights )
    return "No passengers"
