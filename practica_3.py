"""
Vas a observar un diagrama que incluye distintas relaciones y deberás identificar cuáles son y qué representan.
🔹 Qué debés hacer:
1. Identificá todas las relaciones presentes
2. Indicá si son: asociación, herencia, dependencia, agregación o composición
3. Justificá: ¿por qué son de ese tipo?
4. Pensá: ¿qué pasaría si Cliente se borra? ¿Afecta al Pedido?
"""


"""
Grafico

    +-----------+           +-----------------+         +-----------+
    |  Cliente   |◄---------|  Pedido         |-------► |  Producto |
    +-----------+           +-----------------+         +-----------+
                            |                 ▲ 
                            ▼                 |
                            +-----------+     |
                            |  Factura  |-----+
                            +-----------+


1) relaciones presentes:
    - cliente  y pedido: asociacion.
    - pedido y producto: agregacion.
    - pedido y factura: composicion.

2) tipo de relaciones:
    - asociacion.
    - agregacion.
    - composicion.

3) justificacion:
    - El tipo de relacion es asociacion por la clase pedido utiliza a la clase cliente.
    - El tipo de relacion es agregacion por la clase pedido contiene a la clase producto.
    - El tipo de relacion es composicion por la clase pedido contiene a la clase factura.

4) reflexion:
    - Si se borra la clase cliente no afecta a la clase pedido, ya que la relacion es de asociacion.
"""

