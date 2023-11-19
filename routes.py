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
        session["id"] = user_services.get_id(username)
        return redirect("/")
    else:
        return redirect("/")
    
@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    try:
        user_services.create_user(username,password)
        return redirect("/")
    except:
        return redirect("/register")
    
@app.route("/logout")
def logout():
    try:
        del session["username"]
        del session["id"]
    except:
        pass
    return redirect("/")

@app.route("/user")
def user():
    try:
        result = user_services.get_tasks(session["id"])
        tasks=result[0]
        tasks2=result[1]
        return render_template("user.html", tasks=tasks, tasks2=tasks2)
    except:
        return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/task", methods = ["POST"])
def task():
    task=request.form["task"]
    try:
        user_services.add_task(task, session["id"])
        return redirect("/user")
    except:
        return redirect("/user")

@app.route("/mark", methods=["POST"])
def mark():
    task=request.form["task"]
    user_services.mark(task, session["id"])
    return redirect("/user")

@app.route("/reset")
def reset():
    user_services.reset(session["id"])
    return redirect("/user")








