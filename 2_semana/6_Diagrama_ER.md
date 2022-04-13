# Diagrama ER
- Desarrollado por Peter chen en 1976
- Dos entidades.
- Los verbos son las relaciones: como una conexion

- Tecnicas clave del modelado E-R
    - Documentar los tipos d entidades y relaciones de una manera gráfica.

**Se trata de definir un lenguaje comun: lo importante es que todos conozcamos la notacion usada**

## Diferencias entre Diagrama E-R con el Modelo relacional
- mas informacion semantica
- conexiones explicitas entre entidades

# Como se hace el diagrama E-R
- Tipos de entidades
    - Entidad: factura
    - Entidad debil: factura detalles
        - Se enlacen mediante una llave foranea
    - Entidad Asociativa: Empleados-hijos: asociar dos entidades (Relacion N:M)

### Relaciones
- Relaciones:
    - Fuertes:  La existencia de la entidad no depende de la existencia de otra entidad padre.
    - Debiles: Relaciones identificadoras depende de la exixtencia de otra entidad padre.

    - obligatorias:  ___________________________ (simbolo)
    - Opcionales: -------------------------

    - recursivas: empleado__________jefe

### Cardinalidad
- 1:1
- 1:N
- N:M


## Diagrama E-R
- Proceso ciclico:
    - Identificar entidades: 
        - Atributos
        - Llaves
    - Identificar relaciones
        - Laves foraneas
        - Muchos a muchos
    - Diagramar
    - Normalizar
    - Revisar






