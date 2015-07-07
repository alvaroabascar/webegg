# Import Flask framework
# -------------------------------------------------------------------
from flask import Flask, request, redirect, url_for, g

# Import Blueprints
# -------------------------------------------------------------------
from .portfolio.views import portfolio_app

# Start Flask
# -------------------------------------------------------------------
app = Flask(__name__)

# Register Blueprints
# -------------------------------------------------------------------
app.register_blueprint(portfolio_app, url_prefix='/portfolio')
