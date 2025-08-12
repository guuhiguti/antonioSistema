from flask import Blueprint, render_template

clientes_route = Blueprint('clientes', __name__)

@clientes_route.route('/clientes')
def clientes():
    return render_template('clientes.html')