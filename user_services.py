from db import db
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash


class user_services():
    def __init__(self):
        self.users=db.session.execute("select * from users")

    @staticmethod
    def create_user(name, password):
        
        hash_value=generate_password_hash(password)
        sql="insert into users (name, password) values(:name, :password)"
        db.session.execute(text(sql), {"name":name, "password":hash_value})
        db.session.commit()
            
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

#todo tietokantakomennot