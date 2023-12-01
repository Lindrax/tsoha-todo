from flask import render_template, request, redirect, session,flash
from app import app
from user_services import user_services
from db import db
from sqlalchemy.sql import text

@app.route("/")
def index():
    result = user_services.get_tasks(session["id"])
    x= len(result[0])
    y= len(result[1])
    return render_template("index.html", x=x,y=y)

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
    x = user_services.create_user(username,password)
    if x == 1:
        flash("invalid password")
        return redirect("/new")
    if x == 2:
        flash("invalid username")
        return redirect("/new")
    if x == 3:
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
        return render_template("user.html", tasks=tasks, tasks2=tasks2)
    except:
        flash("error")
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
    task=request.form.getlist("task")
    print(task)
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





