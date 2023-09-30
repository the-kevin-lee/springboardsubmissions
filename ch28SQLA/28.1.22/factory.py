# ------------------------- IMPORTS -------------------------------------------
from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Users

#---------------------------CONFIGURATIONS----------------------------------------------
#Main project Setup
factory = Flask(__name__)
factory.config['SECRET_KEY'] = 'something'

#SQLAlchemy Setup 
factory.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly' #setting up SQLA connection to database
factory.config['SQLALCHEMY_ECHO'] = True

#debugger Setup
factory.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(factory)

connect_db(factory)

with factory.app_context():
    db.create_all() # creates the tables within postgresql (used mainly in code editors when developing)


# --------------------------------- CODE ----------------------------------------


@factory.route('/')
def show_home():
    return render_template('home.html')

@factory.route('/users')
def show_users():
    users = Users.query.all()
    return render_template('users.html',users=users)


# new user handling
@factory.route('/users/new', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        image_url = request.form["image_url"]

        print(f"New: First Name: {first_name}, Last Name: {last_name}, Image Url: {image_url}")

        # convert form data into SQLA data
        new_user = Users(first_name=first_name,last_name=last_name,image_url=image_url)
        print(f"New User: {new_user}")
        db.session.add(new_user)
        db.session.commit()
        return redirect('/users')
    else:
        return render_template('adduser.html')
    
# edit user handling
@factory.route('/users/edit/<int:user_id>', methods=['GET','POST'])
def edit_user(user_id):

    identified_user = Users.query.get_or_404(user_id)

    if request.method == 'POST':
        identified_user.first_name = request.form["first_name"]
        identified_user.last_name = request.form["last_name"]
        identified_user.image_url = request.form["image_url"]

        db.session.commit()

        return redirect('/users')
    else:
        return render_template('edituser.html', user=identified_user)
    

#show details route
@factory.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about User"""
    added_user = Users.query.get_or_404(user_id)
    return render_template('showuser.html', added_user=added_user)    


@factory.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Delete user from UI and Database"""
    to_delete_user = Users.query.get_or_404(user_id)
    
    db.session.delete(to_delete_user)
    db.session.commit()
    return redirect(url_for('show_users'))