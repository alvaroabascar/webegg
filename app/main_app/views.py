from flask import Blueprint, render_template

main_app = Blueprint('main_app', __name__,
                     template_folder='templates',
                     static_folder='static')

@main_app.route('/')
def main():
    return render_template("main-index.html")

@main_app.route('/sayhello/<name>')
def sayhello(name):
    return render_template("main-hello.html", name=name)
