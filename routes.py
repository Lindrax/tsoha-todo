
from flask import render_template, request, redirect, session
from app import app
from user_services import user_services
from db import db
from sqlalchemy.sql import text



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if user_services.check_user(username,password):
        session["username"] = username
        return redirect("/")
    else:
        return redirect("/")
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/user")
def user():
    tasks = user_services.get_tasks()
    
    
    
    return render_template("user.html", tasks=tasks)





