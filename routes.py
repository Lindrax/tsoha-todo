
from flask import render_template, request, redirect, session
from app import app
from user_services import user_services
from db import db
from sqlalchemy.sql import text



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/user")
def user():
    tasks = user_services.get_tasks()
    
    
    
    return render_template("user.html", tasks=tasks)





