from datetime import datetime
from jasonsite import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.image_file}', '{self.first_name}', '{self.last_name}')"


class Post(db.Model, UserMixin):
    post_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    title = db.Column(db.String(64), nullable = False)
    date_posted = db.Column(db.String, nullable = False)
    blurb = db.Column(db.String(256), nullable = False)
    content = db.Column(db.Text, nullable = False)
    pill_images = db.relationship('Images', backref = 'post_images', lazy = True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.blurb}', '{self.content}', '{self.pill_images}')"

class Images(db.Model, UserMixin):
    image_id = db.Column(db.Integer, primary_key = True)
    source = db.Column(db.Text, nullable = False)
    posting_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable = False)

    def __repr__(self):
        return f"Images('{self.source}')"
