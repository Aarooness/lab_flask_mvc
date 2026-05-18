from flask import Blueprint, render_template, request, redirect, url_for
from tienda.models.producto import Producto
 
producto_bp = Blueprint("productos", __name__, url_prefix="/productos")
 
@producto_bp.route("/")
def listar():
    productos = Producto.listar_todos()
    return render_template("productos/lista.html", productos=productos)
 
@producto_bp.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = float(request.form["precio"])
        Producto.agregar(nombre, precio)
        return redirect(url_for("productos.listar"))
    return render_template("productos/formulario.html")
