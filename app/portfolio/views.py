from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

portfolio_app = Blueprint('simple_page', __name__,
                        template_folder='templates')

@portfolio_app.route('/', defaults={'page': 'index'})
@portfolio_app.route('/<page>')
def show(page):
    try:
        pagename = '{}.html'.format(page)
        print(pagename)
        return render_template(pagename)
    except TemplateNotFound:
        abort(404)
