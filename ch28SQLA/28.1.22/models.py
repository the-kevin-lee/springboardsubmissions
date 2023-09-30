from flask_sqlalchemy import SQLAlchemy

# initalize and define database to utilize SQLA
db = SQLAlchemy()

# connection to main file
def connect_db(factory):
    db.factory = factory
    db.init_app(factory)
    return db #returns Flask app as an ORM object


# Models

class Users(db.Model):
    """Users"""
    __tablename__ = "Users"

    def __repr__(self):

        u = self
        return f"<User id = {u.id} first_name = {u.first_name} last_name = {u.last_name} image_url = {u.image_url}"
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False, default="First Name")
    last_name = db.Column(db.String(20), nullable=False, default="Last Name")
    image_url = db.Column(db.String, nullable=False, unique=True)





