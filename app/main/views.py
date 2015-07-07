from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main_app = Blueprint('simple_page', __name__,
                     template_folder='templates',
                     static_folder='static')

@main_app.route('/')
def main():
    return render_template('index.html')
