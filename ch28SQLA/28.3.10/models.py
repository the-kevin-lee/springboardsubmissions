from datetime import datetime
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

    posts = db.relationship('Post', backref='user', lazy=True)

class Post(db.Model):
    """Post"""

    __tablename__ = "Post"

    def __repr__(self):
        p = self
        return f"<Post id = {p.id} title = {p.title} content = {p.content} created_at = {p.created_at}"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(20), nullable=False, default="Title")
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_code = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

    tags = db.relationship('Tag', secondary='PostTag', backref='posts') #backref is a SQLA function that allows us to access the tag object from the post object



class PostTag(db.Model):
    
        """PostTag"""
    
        __tablename__ = "PostTag"
    
        def __repr__(self):
            pt = self
            return f"<PostTag id = {pt.id} post_id = {pt.post_id} tag_id = {pt.tag_id}"
    
        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        post_id = db.Column(db.Integer, db.ForeignKey('Post.id'), nullable=False, primary_key=True)
        tag_id = db.Column(db.Integer, db.ForeignKey('Tag.id'), nullable=False, primary_key=True)


class Tag(db.Model):

    """Tag"""

    __tablename__ = "Tag"

    def __repr__(self):
        t = self
        return f"<Tag id = {t.id} name = {t.name}"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

   