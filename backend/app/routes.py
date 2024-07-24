# app/routes.py
from flask import Blueprint, render_template

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/login.html')
def login_page():
    return render_template('login.html')

@routes_bp.route('/register.html')
def register_page():
    return render_template('register.html')