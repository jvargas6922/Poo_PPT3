"""
Grafico 1 (Diagrama de clases basico)

Si requiero poder validar o solitar un tipo de dato en particular para cada atributo

    Atributos privado pero de cualquier tipo de dato
    def __init__(self, nombre, edad):
        self.__nombre = nombre # Atributo privado
        self.__edad = edad # Atributo privado

    Atribitos privados para crear la instancia sean de un tipo en particular
    def __init__(self, nombre:str, edad:int):
        self.__nombre = nombre # Atributo privado
        self.__edad = edad # Atributo privado
"""

class Persona:
    def __init__(self, nombre:str, edad:int):
        self.__nombre = nombre # Atributo privado
        self.__edad = edad # Atributo privado

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
    def cumplir_anios(self):
        self.__edad += 1
        return f"Feliz cumpleaños {self.__nombre}, ahora tienes {self.__edad} años."
    
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    # Setters
    def set_nombre(self, nombre:str):
        self.__nombre = nombre 

    def set_edad(self, edad:int):
        self.__edad = edad
    
# Interpretacion
"""
Grafico de la clase Persona
+------------------+
|     Persona      |
+------------------+
| - __nombre:str   |
| - __edad:int     |
+------------------+
| + saludar()      |
| + cumplir_anios()|
+-----------------+
"""
