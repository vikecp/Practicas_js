# Manejadores
- herramienta interactua
- Son programas 
- asegurar inntegridad de la data
- Recuperacion en caso de falla
- control de accesos 
- manejo de accesos concurrentes

## # componentes importantes en un manejador
1. Data: dueño de la data y el unico que es capaz de manipularla
2. Motor(Database Engine): Son los encargados de acceder  y manipular estos datos 
3. Meta Data: El esquema de nuestra bd, la representacion de nuestro modelo logico el manejador de bd.

# 12 Reglas de Codd
- Regla 0 : un DBSM sea debe ser capaz de manejar bd de manera totalmente relacional

- Regla 1: Regla de la informacion: representado a nivel logico: Valores en tablas.

- Regla 2: Acceso garantizado: Combinacion de: nombre de la tabla, nombre PK, nombre de la columna

- Regla 3: Tratameinto de los valores nulos: debe ser soportables.

- Regla 4: Dicionario dinamico en linea.

- Regla 5: Regla del sub-lenguaje de datos amplio:

- Regla 6: Regla de actualizacion de vistas

- Regla 7: insercion, act, y eliminacion de alto nivel.

- Regla 8: independecia fisica

- Regla 9: Independecia logica

- Regla 10: Independencia de integridad

- Regla 11: Independencia de distribucion

- Regla 12: la regla de no-subversion


