import os
from flask import render_template, url_for, send_from_directory, flash, redirect, request
from jasonsite import app, db, bcrypt
from jasonsite.models import User, Post, Images
from jasonsite.forms import SignUpForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
@app.route("/home")
def home():
    page_title="home"
    return render_template('home.html', title=page_title)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    page_title = "signup"
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password, first_name=form.first_name.data, last_name=form.last_name.data, referral_code=form.referral_code.data )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', title=page_title, form=form)    

@app.route("/login", methods=['GET', 'POST'])
def login():
    page_title = "login"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    return render_template('login.html', title=page_title, form=form)   

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


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
@app.route("/graphic_design")
def graphic_design():
    page_title="Graphic Design"
    return render_template('graphic_design.html', title=page_title)


@app.route("/projects/portfolio")
def portfolio():
    page_title="Portfolio"
    return render_template('portfolio.html', title=page_title)   
# END GRAPHIC DESIGN SECTION


# |--WEB DESIGN SECTION--|
@app.route("/projects/web_design")
def web_design():
    page_title="Web Design"
    project_title= "Template Design"
    project_date= "3/15/2020"

    project_text= "\'Bacon ipsum dolor amet chicken ball tip swine pastrami picanha leberkas bresaola sausage buffalo corned beef tongue tri-tip strip steak biltong shankleKielbasa biltong landjaeger ham hock capicola, jowl pork loin tri-tip ground round cupim corned beef filet mignon chuck boudin.\'"

    project_pill= "/static/images/pills/svg/python_pills.svg"
    return render_template('web_design.html', title=page_title, project_title=project_title, project_date=project_date, project_text=project_text, project_pill=project_pill)


# END WEB DESIGN SECTION
# |--WEB DEVELOPMENT SECTION--|
@app.route("/web_development", methods=['GET', 'POST'])
def web_development():
    page_title="Web Development"
    project_query = Post.query.all()
    project_title= "JasonPonce.Info"
    project_date= "3/15/2020"

    project_text= "\'Bacon ipsum dolor amet chicken ball tip swine pastrami picanha leberkas bresaola sausage buffalo corned beef tongue tri-tip strip steak biltong shankleKielbasa biltong landjaeger ham hock capicola, jowl pork loin tri-tip ground round cupim corned beef filet mignon chuck boudin.\'"

    project_pill= "/static/images/pills/svg/python_pills.svg"
    return render_template('web_development.html', title=page_title, posts=project_query, project_pill=project_pill)

# project_title=project_title, project_date=project_date, project_text=project_text,
@app.route("/web_development/jasonponce_info")
def jasonponce():
    page_title="JasonPonce.Info"
    return render_template('jasonponce_info.html', title=page_title)

@app.route("/test")
def test():
    page_title="test"
    return render_template('test.html', title=page_title)


# END WEB DEVELOPMENT SECTION

