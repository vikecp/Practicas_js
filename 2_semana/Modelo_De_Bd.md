# Modelos de BD
### Historia
- 1960 por parte IBM, manejar todos sus datos sistema para manejo de informacion

- Modelo jerarquico: primera vez se podia relacionar los datos, tenia problemas
- Modelo de redes: modelo complicado dificil de implementar

- 1969: Edgar F. codd ----> le nace la idea de un modelo de bd relacional y genera una revolucion, ven un futuro. soluciona los problemas del modelo jerarquico., Sigue siendo el modelo estandar de la actualidad


## Modelo de archivos planos:
- base del alamacenamiento.
- no sigue ningun formato

- Separar archivos planos: Formatos
- CSV: separa por una coma

- Lenguajes de marcado: html
- Sin formato.

- Archivos binarios: archivos que no son de texto que se puede leer ni entender


## Modelo jerarquico
- apoyado por IMB
- datos organizados de forma jerarquica
- Como arbol invertido
- Nodos se conectan por relaciones
- Camino 
- Padre e hijo si hay relacion
- Dos nodos del mismo nivel se denomina hermanos
    - Este es el gran problema
        - Todas las relaciones son de 1:1
        - no permite la relacion de N:M
- Formatos como el html y el json usan este modelo


## Modelo de redes:
- Busca  solucionar l realcion de N:M

- Basado de la estructura de grafos:
- Ser mas flexible que el modelo jerarquico
- se elimina la duplicidad: menor costos, integridad de datos

- Integridad de los datos: mantener y asegurar la exactitud y consistencia durante toda la vidad de los datos.
- hay varias reglas de integridad.
- caida en 1970, por el nuevo modelo relacional.


## Modelo de Datos relacional
 
- 1969 por primera vez una vision de un modelo relacional por el Dr Edgar Francis. Codd

- Dr Edgar Francis. Codd: cientifico de la computacion, 
- de inglaterra 1923
- programamdor matematico en IBM.

## vision relacional de los datos
- los datos deben describirse en su forma natural
- provee las bases para un lenguaje de consulta de alto nivel
- sienta las bases en : derivibilidad, redundancia y consistencia

- Basada en la teoria de conjuntos y algebra de conjuntos.

- tupla o fila: comjunto de elementos tomados de diferentes dominios
- Cada tupla es un conjunto.
## importancia de los conjuntos
- un conjunto no puede tener elementos
- queda definido por sus miembros
- los conjuntos no tienen orden, tampoco las relaciones.
- los elementos repetidos .


- una relacion no puede tener tuplas repetidas.
- no puede haber dos atributos repetidos(columnas)

### lógica de predicados:
- basados en la logica de 2do orden
- predicado: es una expresion que se evalua a un valor de verdad


