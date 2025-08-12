from flask import Blueprint, render_template

produtos_route = Blueprint('produtos', __name__)

@produtos_route.route('/produtos')
def produtos():
    return render_template('produtos.html')