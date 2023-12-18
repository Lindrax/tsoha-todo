from flask import render_template, request, redirect, session,flash
from app import app
from user_services import user_services
from db import db
from sqlalchemy.sql import text
import secrets

@app.route("/")
def index():
    try:
        result = user_services.get_tasks(session["id"])
        done= len(result[0])
        undone= len(result[1])
        tasks=user_services.get_ded(session["id"])
        return render_template("index.html", x=done,y=undone, tasks=tasks)
    except:
        return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if user_services.check_user(username,password):
        session["username"] = username
        session["id"] = user_services.get_id(username)
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")
    else:
        flash("login error")
        return redirect("/")
    
@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    error = user_services.create_user(username,password)
    if error == 1:
        flash("invalid password")
        return redirect("/new")
    if error == 2:
        flash("invalid username")
        return redirect("/new")
    if error == 3:
        flash("username taken")
        return redirect("/new")
    else:
        flash("succesfully registered")
        return redirect("/")

   
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
        tasks2=result[1][-5:]
        cats = user_services.get_cats(session["id"])
        return render_template("user.html", tasks=tasks, tasks2=tasks2, cats =cats)
    except:
        flash("error")
        return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/task", methods = ["POST"])
def task():
    if session["csrf_token"] != request.form["csrf_token"]:
        flash("abort(403)")

    task=request.form["task"]
    try:
        cat=request.form["category"]
    except:
        cat="NULL"
    try:
       deadline=request.form["deadline"]
    except:
        deadline="NULL"

    user_services.add_task(task, session["id"], cat, deadline)
    return redirect("/user")
    

@app.route("/mark", methods=["POST"])
def mark():
    task=request.form.getlist("task")
    for i in task:
        user_services.mark(i, session["id"])
    return redirect("/user")

@app.route("/reset")
def reset():
    user_services.reset(session["id"])
    return redirect("/user")

@app.route("/done")
def done():
    result = user_services.get_tasks(session["id"])
    tasks=result[1]
    return render_template("done.html", tasks=tasks)

@app.route("/delete", methods=["POST"])
def delete():
    task=request.form.getlist("task")
    for i in task:
        user_services.delete(i, session["id"])
    return redirect("/done")

@app.route("/newcat")
def newcat():
    return render_template("newcat.html")

@app.route("/addcat", methods=["POST"])
def addcat():
    cat=request.form["category"]
    col=request.form["col"]
    user_services.add_cat(cat, session["id"], col)
    return redirect("/user")

