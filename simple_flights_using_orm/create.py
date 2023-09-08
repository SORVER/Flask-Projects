import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

# we may use pip3 install flask-session
app = Flask(__name__)
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
 # tells the file where to fund the databse
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # turn off autimatic changes "it used in Debuging"

db.init_app(app) # bind the database with the app


def main():
    db.create_all()

# single / for the home
# just time it differnt in every browser (not same at all users)
if __name__ == "__main__":
    with app.app_context(): #rules in flask
        main()