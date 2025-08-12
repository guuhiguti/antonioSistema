from flask import Flask
from routes.home import home_route
from routes.produtos import produtos_route
from routes.clientes import clientes_route
from routes.pedidos import pedidos_route

app = Flask(__name__)
app.register_blueprint(home_route)
app.register_blueprint(produtos_route)
app.register_blueprint(clientes_route)
app.register_blueprint(pedidos_route)

app.run(debug=True)