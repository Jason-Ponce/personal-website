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
    page_title="home"
    return render_template('home.html', title=page_title)


@app.route("/about")
def about():
    page_title="about"
    return render_template('about.html', title=page_title)


@app.route("/resume")
def resume():
    page_title="Resume"
    return render_template('resume.html', title=page_title)


@app.route("/projects")
def projects():
    page_title="projects"
    return render_template('projects.html', title=page_title)

# |--GRAPHIC DESIGN SECTION--|
@app.route("/projects/graphic_design")
def graphic_design():
    page_title="Graphic Design"
    return render_template('graphic_design.html', title=page_title)

@app.route("/projects/graphic_design/case_studies")
def case_studies():
    page_title="Case Studies"
    return render_template('case_studies.html', title=page_title)


@app.route("/projects/graphic_design/case_studies/form_storming")
def form_storming():
    page_title="Form Storming"
    return render_template('form_storming.html', title=page_title)


@app.route("/projects/graphic_design/photoshop_experiments")
def photoshop_experiments():
    page_title="Photoshop Experiments"
    return render_template('photoshop_experiments.html', title=page_title)    


@app.route("/projects/graphic_design/photoshop_experiments/EXPLOSION")
def EXPLOSION():
    page_title="EXPLOSION"
    return render_template('EXPLOSION.html', title=page_title)    


@app.route("/projects/graphic_design/photoshop_experiments/underwater_effect")
def underwater_effect():
    page_title="Underwater Effect"
    return render_template('underwater_effect.html', title=page_title)    


@app.route("/projects/graphic_design/photoshop_experiments/smudge_script")
def smudge_script():
    page_title="Smudge Script"
    return render_template('smudge_script.html', title=page_title)    

    
# END GRAPHIC DESIGN SECTION
# |--WEB DESIGN SECTION--|
@app.route("/projects/web_design")
def web_design():
    page_title="Web Design"
    return render_template('web_design.html', title=page_title)


# END WEB DESIGN SECTION
# |--WEB DEVELOPMENT SECTION--|
@app.route("/projects/web_development")
def web_development():
    page_title="Web Development"
    return render_template('web_development.html', title=page_title)


# END WEB DEVELOPMENT SECTION

# TESTING 
# GROUNDS
# FOR
# STUFF
# @app.route("/testing_grounds")
# def testing_grounds():
#     page_title="testing grounds"
#     return render_template('projects_index.html', title=page_title)


