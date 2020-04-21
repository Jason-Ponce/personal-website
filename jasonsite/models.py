from datetime import datetime
from jasonsite import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(120), unique=True, nullable=False)
    profile_image   = db.Column(db.String(20), nullable=False, default='default.png')
    password        = db.Column(db.String(60), nullable=False)
    first_name      = db.Column(db.String(64), nullable=False)
    last_name       = db.Column(db.String(64), nullable=False)
    status          = db.Column(db.Boolean, nullable=False)
    posts           = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.status}', '{self.first_name}', '{self.last_name}')"


class Post(db.Model, UserMixin):
    post_id         = db.Column(db.Integer, primary_key = True)
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    title           = db.Column(db.String(64), nullable = False)
    date_posted     = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    blurb           = db.Column(db.String(256), nullable = False)
    post            = db.Column(db.Text, nullable = False)
    images          = db.relationship('Images', backref = 'post_images', lazy = True)
    category        = db.Column(db.String(32), nullable = False)
    created_by      = db.relationship('User', backref = 'owner', lazy=True)
    more_posts      = db.relationship('Content', backref= 'test_txt', lazy = True)
    tag1            = db.Column(db.Text, nullable = False)
    tag2            = db.Column(db.Text, nullable = False)
    tag3            = db.Column(db.Text, nullable = False)
    tag4            = db.Column(db.Text, nullable = False)
    tag5            = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.blurb}', '{self.date_posted}', '{self.post}', '{self.category }', '{self.post_id}')"


class Images(db.Model, UserMixin):
    image_id        = db.Column(db.Integer, primary_key = True)
    source          = db.Column(db.Text, nullable = False)
    alt_source      = db.Column(db.Text, nullable = False)
    posting_id      = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable = False)
    category        = db.Column(db.String(32), nullable = False)

    def __repr__(self):
        return f"Images('{self.source}')"


class Content(db.Model, UserMixin):
    extendedpost_id = db.Column(db.Integer, primary_key = True)
    posting_id      = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable = False)
    content_post    = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"Content('{self.content_post}')"