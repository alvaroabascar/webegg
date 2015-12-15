# Import Flask framework
# -------------------------------------------------------------------
from flask import Flask, request, redirect, url_for, g

# Import Blueprints
# -------------------------------------------------------------------
from .main_app.views import main_app
from .other_app.views import other_app

# Start Flask
# -------------------------------------------------------------------
app = Flask(__name__, static_folder='main_app/static')

# Register Blueprints
# -------------------------------------------------------------------
app.register_blueprint(main_app, url_prefix='')
app.register_blueprint(other_app, url_prefix='/other')
