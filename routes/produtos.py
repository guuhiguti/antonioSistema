from flask import Blueprint, render_template

produtos_route = Blueprint('produtos', __name__, url_prefix='/produtos')

@produtos_route.route('/')
def produtos():
    return render_template('produtos.html')

@produtos_route.route('/estoque')
def estoque():
    return render_template('estoque.html')