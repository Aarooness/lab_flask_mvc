from flask import Flask, render_template_string, request, redirect, url_for
 
app = Flask(__name__)
 
# Datos en memoria (mala práctica en producción)
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 3500.00},
    {"id": 2, "nombre": "Mouse", "precio": 45.50},
    {"id": 3, "nombre": "Teclado", "precio": 120.00}
]
 
@app.route("/")
def inicio():
    return "<h1>Bienvenido a la tienda</h1><a href='/productos'>Ver productos</a>"
 
@app.route("/productos")
def listar_productos():
    html = "<h1>Productos</h1><ul>"
    for prod in productos:
        html += f"<li>{prod['nombre']} - S/ {prod['precio']}</li>"
    html += "</ul>"
    return html
 
@app.route("/productos/agregar", methods=["GET", "POST"])
def agregar_producto():
    if request.method == "POST":
        nuevo = {
            "id": len(productos) + 1,
            "nombre": request.form["nombre"],
            "precio": float(request.form["precio"])
        }
        productos.append(nuevo)
        return redirect(url_for("listar_productos"))
    return '''
        <form method="POST">
            Nombre: <input name="nombre"><br>
            Precio: <input name="precio" type="number" step="0.01"><br>
            <button type="submit">Agregar</button>
        </form>
    '''
 
if __name__ == "__main__":
    app.run(debug=True)
