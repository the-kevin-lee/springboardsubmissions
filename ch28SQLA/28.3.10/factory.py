# ------------------------- IMPORTS -------------------------------------------
from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Users, Post, Tag, PostTag

#---------------------------CONFIGURATIONS----------------------------------------------
#Main project Setup
factory = Flask(__name__)
factory.config['SECRET_KEY'] = 'something'

#SQLAlchemy Setup 
factory.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly' #setting up SQLA connection to database
factory.config['SQLALCHEMY_ECHO'] = False #turns off SQLA logging

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

#delete user route
@factory.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Delete user from UI and Database"""
    to_delete_user = Users.query.get_or_404(user_id)
    
    db.session.delete(to_delete_user)
    db.session.commit()
    return redirect(url_for('show_users'))

#################### POST ROUTES ######################


# new post handling
@factory.route('/users/<int:user_id>/posts/new', methods=['GET','POST'])
def add_post(user_id):
    """Add a post for a user"""
    all_tags = Tag.query.all()  # Query all available tags
    
    if request.method == 'POST':
        title = request.form["post_title"]
        content = request.form["post_content"]

        new_post = Post(title=title, content=content, user_code=user_id)
        
        selected_tags = request.form.getlist("post_tags[]")

        for tag_id in selected_tags:
            tag = Tag.query.get(tag_id)
            new_post.tags.append(tag)

        db.session.add(new_post)
        db.session.commit()
        return redirect(f'/users/{user_id}')
    else:
        return render_template('newpost.html', user_id=user_id, tags=all_tags)

    
# show post route
@factory.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show post details"""
    added_post = Post.query.get_or_404(post_id)
    return render_template('showpost.html', added_post=added_post)

# edit post route
@factory.route('/posts/<int:post_id>/edit', methods=['GET','POST'])
def edit_post(post_id):
    """Edit post"""
    identified_post = Post.query.get_or_404(post_id)
    all_tags = Tag.query.all()

    if request.method == 'POST':
        identified_post.title = request.form["post_title"]
        identified_post.content = request.form["post_content"]

        selected_tags = request.form.getlist("post_tags[]")
        identified_post.tags = []

        for tag_id in selected_tags:
            tag = Tag.query.get(tag_id)
            identified_post.tags.append(tag)

        db.session.commit()

        return redirect(f'/posts/{post_id}')
    else:
        return render_template('editpost.html', post=identified_post, tags=all_tags)
    

# delete post route
@factory.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Delete post"""
    to_delete_post = Post.query.get_or_404(post_id)
    user_id = to_delete_post.user_code
    db.session.delete(to_delete_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')


#################### TAG ROUTES ######################


# create tag route
@factory.route('/tags/new', methods=['GET','POST'])
def add_tag():
    """Add a tag"""
    if request.method == 'POST':
        tag_name = request.form['tag_name']
        new_tag = Tag(name=tag_name)

        db.session.add(new_tag)
        db.session.commit()
        return redirect('/tags')
    else:
        return render_template('addtag.html')
    
# edit tag route
@factory.route('/tags/<int:tag_id>/edit', methods=['GET','POST'])
def edit_tag(tag_id):
    """Edit tag"""
    identified_tag = Tag.query.get_or_404(tag_id)

    if request.method == 'POST':
        identified_tag.name = request.form["tag_name"]

        db.session.commit()

        return redirect('/tags')
    else:
        return render_template('edittag.html', tag=identified_tag)

# list tags route
@factory.route('/tags')
def list_tags():
    """Show all tags"""
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)



# show tag route
@factory.route('/tags/<int:tag_id>')
def show_tag(tag_id):
    """Show tag details"""
    added_tag = Tag.query.get_or_404(tag_id)
    return render_template('showtag.html', added_tag=added_tag)