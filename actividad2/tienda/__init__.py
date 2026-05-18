from flask import Flask
 
def create_app():
    app = Flask(__name__)
 
    from tienda.controllers.producto_controller import producto_bp
    app.register_blueprint(producto_bp)
 
    @app.route("/")
    def inicio():
        return "<h1>Tienda MVC</h1><a href='/productos/'>Ver productos</a>"
 
    return app
