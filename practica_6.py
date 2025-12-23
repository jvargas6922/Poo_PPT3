"""
Contexto: 🙌
Un equipo junior diseñó el siguiente modelo UML para un sistema de e-commerce. Tu tarea es detectar
errores conceptuales y reformularlo correctamente.
Consigna: ✍
Diagrama (descripción):
    ● Cliente: -nombre, -email, +comprar() (listo)
    ● Carrito: -productos, +agregar(), +vaciar() (listo)
    ● Producto: -nombre, -precio (listo)
    ● Factura: +total, +imprimir() (listo)
Relaciones:
    ● Cliente hereda de Carrito (incorrecto)
    ● Factura depende de Producto (no de Carrito)
    ● Carrito está unido a Producto con flecha simple sin multiplicidad
    ● Todos los métodos están públicos, pero los atributos también
"""

class Cliente:
    def __init__(self, nombre:str, email:str):
        self.__nombre = nombre
        self.__email = email

    def comprar(self):
        """
            Método para realizar una compra.
        """
        pass

    # Getters
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_email(self) -> str:
        return self.__email
    
    # Setters
    def set_nombre(self, nombre:str):
        self.__nombre = nombre

    def set_email(self, email:str):
        self.__email = email

class Carrito:
    def __init__(self, productos:list):
        self.__productos = productos

    def agregar(self, producto):
        """
            Método para agregar un producto al carrito.
        """
        self.__productos.append(producto)

    def vaciar(self):
        """
            Método para vaciar el carrito.
        """
        self.__productos.clear()

    # Getter
    def get_productos(self) -> list:
        return self.__productos
    
    # setter
    def set_productos(self, productos:list):
        self.__productos = productos

class Producto:
    def __init__(self, nombre:str, precio:float):
        self.__nombre = nombre
        self.__precio = precio

    # Getters
    def get_nombre(self)->str:
        return self.__nombre
    
    def get_precio(self)->str:
        return self.__precio
    
    # Setters
    def set_nombre(self, nombre:str):
        self.__nombre = nombre

    def set_precio(self, precio:float):
        self.__precio = precio

class Factura:
    def __init__(self, total:float):
        self.total = total

    def imprimir(self):
        """
            Método para imprimir la factura.
        """
        pass

"""
Correcciones:
    1)
        - Cliente hereda de Carrito(Incorrecto)
        - Carrito no hereda de Cliente(Correcto)
    2) 
        - Factura depende de Producto (no de Carrito) (Incorrecto)
        - Factura depende del Carrito (Correcto)
    3)
        - Carrito está unido a Producto con flecha simple sin multiplicidad(Incorrecto)
        - Carrito está unido a Producto con flecha simple con multiplicidad (Correcto)
    4)
        - Todos los métodos están públicos, pero los atributos también(Incorrecto por los atributos estan privados)
"""

"""
Grafico UML Incorrecto:
    +----------------+          +----------------+          +----------------+          +----------------+
    |    Cliente     |          |    Carrito     |          |    Producto    |          |    Factura     |
    +----------------+          +----------------+          +----------------+          +----------------+
    | -nombre        |          | -productos     |          | -nombre        |          | +total         |
    | -email         |          +----------------+          | -precio        |          | +imprimir()    |
    +----------------+          | +agregar()     |          +----------------+          +----------------+
    | +comprar()     |          | +vaciar()      |          |                |          |                |
    +----------------+          +----------------+          +----------------+          +----------------+
          ^                           |                                   ^                           |
          |                           |                                   |                           |
          +---------------------------+                                   |                            
                                                                          |                           
                      Herencia Incorrecta                          Dependencia Incorrecta
"""


"""""
Grafico UML Correcto:

    +----------------+          +----------------+          +----------------+          +----------------+
    |    Cliente     |          |    Carrito     |          |    Producto    |          |    Factura     |
    +----------------+          +----------------+          +----------------+          +----------------+
    | -nombre        |          | -productos     |          | -nombre        |          | +total         |
    | -email         |          +----------------+          | -precio        |         
    +----------------+          | +agregar()     |          +----------------+          +----------------+
    | +comprar()     |          | +vaciar()      |          |                |          |  +imprimir()   |
    +----------------+          +----------------+          +----------------+          +----------------+  
          |                           |                                   |                              |
          |                           |                                   |                              |
          +---------------------------+                                   |                              |   
                                                                          |                              |
                                                                          |+-----------------------------+      
                                                                                Dependencia Correcta

"""