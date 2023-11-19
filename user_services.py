from db import db
from sqlalchemy.sql import text


class user_services():
    def __init__(self):
        self.users=db.session.execute("select * from users")


    def get_tasks():
        sql="SELECT task FROM tasks"
        result = db.session.execute(text(sql)).fetchall()
        
        return result
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