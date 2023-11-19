from db import db
from sqlalchemy.sql import text


class user_services():
    def __init__(self):
        self.users=db.session.execute("select * from users")

    @staticmethod
    def get_tasks(user_id):
        sql="SELECT task FROM tasks where user_id=:user_id"
        result = db.session.execute(text(sql), {"user_id":user_id}).fetchall()
        return result

    @staticmethod
    def get_id(name):
        try:
            sql="select id from users where name=:name"
            result = db.session.execute(text(sql), {"name":name}).fetchone()
            return result[0]
        except:
            return []
        
        
    
    #def add_task(task, user):
        sql="insert tasks (task, user_id) values (:task, :user)"
        db.session.execute(text(sql), {task:task, user:user})

    @staticmethod
    def check_user(user, password):
        sql="select password from users where name =:user"
        result=db.session.execute(text(sql), {"user":user} ).fetchone()
        try:
            if result[0] == password:
                return True
        except:
            return False

#todo tietokantakomennot