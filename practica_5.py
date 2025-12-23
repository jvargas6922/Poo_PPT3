"""
Una aerolínea representa su sistema de reservas mediante UML. 
Te dan el diagrama y necesitás entender la lógica y relaciones entre las clases.
Consigna: ✍
Analizá el siguiente conjunto de clases:
    ● Pasajero: tiene +nombre, +dni, +email (listo)
    ● Reserva: tiene +codigo, +fecha, +estado (listo)
    ● Vuelo: tiene +origen, +destino, +hora, +avion (listo)
    ● Avion: tiene +modelo, +capacidad

Relaciones UML (descritas):
    ● Un Pasajero puede tener muchas Reservas (1 a *) (listo)
    ● Cada Reserva pertenece a un único Vuelo (1 a 1) (listo)
    ● Cada Vuelo está compuesto por un Avion (listo)
    ● Reserva y Pasajero están asociada (listo)
-----------------------------------------------
Paso a paso: ⚙
1.Dibujá el diagrama de clases completo con las relaciones correctas (listo)
2. Indicá visibilidad de atributos y métodos (listo)
3. Explicá cada tipo de relación (listo)
4. Justificá por qué se usó composición o asociación en cada caso
"""

class Pasajero:
    def __init__(self, nombre:str, dni:str, email:str):
        self.nombre = nombre
        self.dni = dni
        self.email = email

    def datos_pasajero(self)-> str:
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Email: {self.email}"

class Reserva:
    def __init__(self,codigo:str, fecha:str, estado:str):
        self.codigo = codigo
        self.fecha = fecha
        self.estado = estado

    def datos_reserva(self)->str:
        return f"Código: {self.codigo}, Fecha: {self.fecha}, Estado: {self.estado}"

class Vuelo:
    def __init__(self,origen:str, destino:str, hora:str, avion:str):
        self.origen = origen
        self.destino = destino
        self.hora = hora
        self.avion = avion

    def datos_vuelo(self)->str:
        return f"Origen: {self.origen}, Destino: {self.destino}, Hora: {self.hora}, Avion: {self.avion}"

class Avion:
    def __init__(self, modelo:str, capacidad:int):
        self.modelo = modelo
        self.capacidad = capacidad
    
    def info_avion(self)->str:
        return f"Modelo: {self.modelo}, Capacidad: {self.capacidad}"


# intancias de las clases para probar los atributos y metodos
# pasajero_1 = Pasajero("Pedro","12345678-9","pedro@gmail.com")
# print(pasajero_1.datos_pasajero())

"""
Realcion entre clases(Entidades) 
-  1 -> 1 (Uno a Uno): Cada instancia de una clase está asociada con una única instancia de otra clase.
    Ejemplo de  1 a 1 => un usuario tiene un perfil.

- 1 -> (*) = (N) (Uno a Muchos): Una instancia de una clase puede estar asociada con múltiples instancias de otra clase.
    Ejemplo de 1 a muchos => factura tiene muchos productos.

- (*) -> (*) = (N a N) (Muchos a Muchos): Múltiples instancias de una clase pueden estar asociadas con múltiples instancias de otra clase.
    Ejemplo de muchos a muchos => estudiantes y cursos.

"""


"""
    +----------+
    | Pasajero |
    +----------+
            1
            |
            |
            *
    +----------+            +----------+
    | Reserva  |1 -------- 1|  Vuelo   |
    +----------+            +----------+
                                |
                                |
                                1
                            +----------+
                            |  Avion   |
                            +----------+    

1) Relaciones entre clases:
    - Un pasajero puede tener muchas reservas (1 a *) 
    - Cada reserva pertenece a un unico vuelo  (1 a 1)  
    - Un vuelo esta compuesto por un avion
    - Reserva y Pasajero estan asociada (asociacion)   

2) Atributos y Metodos:
    - Pasajero
        * Atributos: nombre, dni, email
        * Métodos: datos_pasajero() 

    - Reserva 
        * Atributos: codigo, fecha, estado
        * Métodos: datos_reserva()

    - Vuelo
        * Atributos: origen, destino, hora, avion
        * Métodos: datos_vuelo()

    - Avion
        * Atributos: modelo, capacidad
        * Métodos: info_avion()         
"""