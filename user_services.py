from db import db
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import time

class user_services():
    def __init__(self):
        self.users=db.session.execute("select * from users")
        self.us={}
        

    @staticmethod
    def create_user(name, password):
        #1 = passwqord too short or long
        #2 = name too short or long
        #3 username taken

        if len(password) >20 or len(password) <1:
            return 1
        if len(name) > 20 or len(name) <1:
            return 2
        print(db.session.execute(text("select name from users")).fetchall())
        
        if len(db.session.execute(text("select name from users where name=:name"), {"name":name}).fetchall()) ==0:
            hash_value=generate_password_hash(password)
            sql="insert into users (name, password) values(:name, :password)"
            db.session.execute(text(sql), {"name":name, "password":hash_value})
            db.session.commit()
            
        else:
            return 3
 
            
    @staticmethod
    def get_tasks(user_id):
        sql="SELECT * FROM tasks where user_id=:user_id and done is FALSE and del is false"
        result = db.session.execute(text(sql), {"user_id":user_id}).fetchall()
        sql2="SELECT * FROM tasks where user_id=:user_id and done is true and del is false"
        result2 = db.session.execute(text(sql2), {"user_id":user_id}).fetchall()
        return (result, result2)

    @staticmethod
    def get_id(name):
        sql="select id from users where name=:name"
        result = db.session.execute(text(sql), {"name":name}).fetchone()
        return result[0]


    @staticmethod
    def check_user(user, password):
        sql="select password from users where name =:user"
        result=db.session.execute(text(sql), {"user":user} ).fetchone()
        if not result:
            return False
        else:
            try:
                if check_password_hash(result.password, password):
                    return True
            except:
                return False
            
    @staticmethod
    def add_task(task, user_id, cat, deadline):
        atm=datetime.date.today()
        sql2="select color from categories where category =:cat"
        col=db.session.execute(text(sql2), {"cat":cat}).fetchone()[0]
        sql="insert into tasks (task, user_id, time, category, deadline, col) values (:task, :user_id, :atm, :cat, :deadline, :col)"
        db.session.execute(text(sql), {"task":task, "user_id":user_id, "atm":atm, "cat":cat, "deadline":deadline, "col":col})
        db.session.commit()
    
    
    @staticmethod
    def mark(task, user_id):
        t=datetime.date.today()
        sql="update tasks set done = (TRUE) where task=:task and user_id=:user_id"
        sql2="insert into done (task, user_id, time) values (:task, :user_id, :t)"
        db.session.execute(text(sql), {"task":task, "user_id":user_id})
        db.session.execute(text(sql2), {"task":task, "user_id":user_id, "t":t})
        db.session.commit()
    

    @staticmethod
    def reset(user_id):
        sql="delete from tasks where user_id=:user_id"
        db.session.execute(text(sql), {"user_id":user_id})
        db.session.commit()

    @staticmethod
    def delete(task, user_id):
        sql="update tasks set del = (TRUE) where task=:task and user_id=:user_id"
        db.session.execute(text(sql), {"task":task, "user_id":user_id})
        db.session.commit()

    @staticmethod
    def get_cats(user_id):
        sql="select * from categories where user_id=:user_id"
        result = db.session.execute(text(sql), {"user_id":user_id}).fetchall()
        return result
    
    @staticmethod
    def add_cat(category, user_id, color):
        sql="insert into categories (category, user_id, color) values ( :category, :user_id, :color)"
        db.session.execute(text(sql), {"category":category, "user_id":user_id, "color":color})
        db.session.commit()