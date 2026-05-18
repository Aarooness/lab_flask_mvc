class Producto:
    """Representa un producto del catálogo."""
 
    _productos = [
        {"id": 1, "nombre": "Laptop", "precio": 3500.00},
        {"id": 2, "nombre": "Mouse", "precio": 45.50},
        {"id": 3, "nombre": "Teclado", "precio": 120.00}
    ]
 
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
 
    @classmethod
    def listar_todos(cls):
        return [cls(**p) for p in cls._productos]
 
    @classmethod
    def agregar(cls, nombre, precio):
        nuevo_id = max([p["id"] for p in cls._productos], default=0) + 1
        cls._productos.append({"id": nuevo_id, "nombre": nombre, "precio": precio})
        return cls(nuevo_id, nombre, precio)
 
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "precio": self.precio}
