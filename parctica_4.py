"""
¿En qué consistirá la Demo?
Te presento un pequeño sistema representado en UML, y deberás analizarlo de forma estructurada.
1. Identificá los nombres de clases y sus atributos/métodos
2. Determiná el tipo de relación entre cada clase
3. Analizá si están bien representadas la visibilidad y los métodos
4. Respondé: ¿podría Carrito existir sin Usuario? ¿Y sin Producto?
🔹 Diagrama propuesto (descripción):
Clase Usuario:
    ● +nombre: String, +email: String, +login(): bool
Clase Carrito:
    ● -productos: List<Producto>, +agregarProducto(),
    +calcularTotal(): float
    ● Composición con Producto
Clase Producto:
    ● +nombre: String, +precio: float
Relación:
    ● Usuario está asociado con Carrito
    ● Carrito está compuesto por Producto
"""

class Usuario:
    def __init__(self, nombre:str, email:str):
        self.nombre = nombre
        self.email = email

    def login(self)->bool:
        """ se puede simular que se reciben los datos de la instancia
            y se valida contra unos datos harcodeados 
        """
        pass

#-------------------->
class Carrito:
    def __init__(self, productos:list):
        self.__productos = productos

    def agregar_producto(self, producto):
        """ agrega un producto a la lista de productos """
        pass

    def calcular_total(self)->float:
        """ calcula el total de los precios de los productos en el carrito """
        pass
    
    # Getter
    def get_productos(self)->list:
        return self.__productos
    
    # Setter
    def set_productos(self, productos:list):
        self.__productos = productos


#-------------------->
class Producto:
    def __init__(self, nombre:str, precio:float):
        self.nombre = nombre
        self.precio = precio

""""
Grafico
    +-----------+           +-----------------+
    |  Usuario   |◄---------|    Carrito      |
    +-----------+           +-----------------+         
                            |                 ▲ 
                            ▼                 |
                            +-----------+     |
                            |  Producto |-----+
                            +-----------+


1) 
    - Clase: 
        Usuario 
        Carrito
        Producto

    - Atributos:
        Usuario: nombre, email
        Carrito: productos
        Producto: nombre, precio

    - Metodos:
        Usuario: login()
        Carrito: agregar_pructo(), calcular_total()
        Producto: None

2) tipo de relaciones:
    - Usuario y Carrito: asociacion.
    - Carrito y Producto: composicion.



"""
