import os
from flask import render_template, url_for, send_from_directory
from jasonsite import app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
@app.route("/web_development")
def web_development():
    page_title="Web Development"
    project_title= "JasonPonce.Info"
    project_date= "3/15/2020"

    project_text= "\'Bacon ipsum dolor amet chicken ball tip swine pastrami picanha leberkas bresaola sausage buffalo corned beef tongue tri-tip strip steak biltong shankleKielbasa biltong landjaeger ham hock capicola, jowl pork loin tri-tip ground round cupim corned beef filet mignon chuck boudin.\'"

    project_pill= "/static/images/pills/svg/python_pills.svg"
    return render_template('web_development.html', title=page_title, project_title=project_title, project_date=project_date, project_text=project_text, project_pill=project_pill)


@app.route("/web_development/jasonponce_info")
def jasonponce():
    page_title="JasonPonce.Info"
    return render_template('jasonponce_info.html', title=page_title)

@app.route("/test")
def test():
    page_title="test"
    return render_template('test.html', title=page_title)


# END WEB DEVELOPMENT SECTION

# TESTING 
# GROUNDS
# FOR
# STUFF
# @app.route("/testing_grounds")
# def testing_grounds():
#     page_title="testing grounds"
#     return render_template('projects_index.html', title=page_title)


