from db import db
from sqlalchemy.sql import text


class user_services():
    def get_tasks():
        sql="SELECT task FROM tasks"
        result = db.session.execute(text(sql)).fetchall()
        
        return result
#todo tietokantakomennot