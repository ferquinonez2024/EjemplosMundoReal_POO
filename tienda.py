# Archivo: tienda.py

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Carrito:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_carrito(self):
        if not self.productos:
            print("Carrito vacío")
        else:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(producto)
    
    def calcular_total(self):
        total = sum([producto.precio for producto in self.productos])
        return total

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear algunos productos
    producto1 = Producto("Camiseta", 250)
    producto2 = Producto("Pantalón", 400)
    
    # Crear un carrito
    carrito = Carrito()
    
    # Agregar productos al carrito
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)
    
    # Mostrar productos en el carrito
    carrito.mostrar_carrito()
    
    # Calcular total
    total = carrito.calcular_total()
    print(f"Total a pagar: ${total}")
