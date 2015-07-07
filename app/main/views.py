from flask import Blueprint, render_template

main_app = Blueprint('main_app', __name__,
                     template_folder='templates')

@main_app.route('/')
def main():
    return "HI"

@main_app.route('/sayhello/<name>')
def sayhello(name):
    return render_template("hello.html", name=name)
