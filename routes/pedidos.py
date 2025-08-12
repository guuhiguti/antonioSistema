from flask import Blueprint, render_template

pedidos_route = Blueprint('pedidos', __name__)

@pedidos_route.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')