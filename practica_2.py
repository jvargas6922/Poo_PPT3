"""
Vas a analizar un ejemplo simple de diagrama de clase para identificar correctamente su nombre, atributos,
métodos y visibilidad.
1.Identificá el nombre de la clase (Producto) listo
2. Listá los atributos, sus tipos y visibilidad (codigo:int privado, nombre:str privado, precio:float privado) listo
3. Indicá cuántos métodos tiene y qué hacen
4. Determiná si alguno modifica atributos o devuelve un valor
5. Reflexioná: ¿esta clase está bien diseñada? ¿Qué le falta?
"""

class Producto:
    def __init__(self, codigo:int, nombre:str, precio:float):
        self.__codigo = codigo          # Atributo privado
        self.__nombre = nombre          # Atributo privado
        self.__precio = precio          # Atributo privado

    def mostrar_info(self) -> str:
        """Devuelve una cadena con la información del producto."""
        return f"Código: {self.__codigo}, Nombre: {self.__nombre}, Precio: {self.__precio}"
    
    def aplicar_descuento(self, porcentaje:float) -> None:
        """Aplica un descuento al precio del producto."""
        if 0 < porcentaje < 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento

    # Getters
    def get_codigo(self) -> int:
        return self.__codigo
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_precio(self) -> float:
        return self.__precio
    
    # Setters
    def set_codigo(self, codigo:int) -> None:
        self.__codigo = codigo

    def set_nombre(self, nombre:str) -> None:
        self.__nombre = nombre

    def set_precio(self, precio:float) -> None:
        self.__precio = precio

# intrerpretacion
"""
Grafico de la clase Producto
+----------------------+
|      Producto         |
+----------------------+
| - __codigo:int       |
| - __nombre:str       |
| - __precio:float     |
+----------------------+
| + mostrar_info()     |
| + aplicar_descuento()|
+----------------------+
"""
    
    


