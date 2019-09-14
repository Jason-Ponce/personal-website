import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from jasonsite import app, db, bcrypt
# from jasonsite.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
# from jasonsite.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')



