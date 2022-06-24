from flask import Flask, render_template, abort
import os

template_dir = os.path.abspath("portofolio/templates_fs")
static_dir = os.path.abspath("portofolio/static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

projects = [{
        "name": "Habit tracking app with Python, Flask Framework, and MongoDB",
        "thumb": "img/habit-tracking.jpg",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://wibawaarif-habitracker.herokuapp.com/"
        },
        {
        "name": "Microblog app with Python, Flask Framework, and MongoDB",
        "thumb": "img/microblog.jpg",
        "hero": "img/microblog-hero.jpg",
        "categories": ["python", "web"],
        "slug": "microblog",
        "prod": "https://wibawaarif-microblog.herokuapp.com/"
        },
        {
        "name": "Simple investment quiz app with Python, Flask Framework, and MongoDB",
        "thumb": "img/quiz.jpg",
        "hero": "img/quiz-hero.jpg",
        "categories": ["python", "web"],
        "slug": "quiz-app",
        "prod": "https://wibawaarif-quizapp.herokuapp.com/"
        }]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", 
                            project=slug_to_project[slug]
                            )
        
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
