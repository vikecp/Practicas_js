# SQL Structured Query Language
- origen 1974 por ibm system R por Donald y Raymond Boyce
- 1986 SQL Standard ANSI
- 1987 SQL Standard ISO

# Regla del sublenguaje de datos amplio SQL

- DDL: lenguaje de definicion de datos:
    - Comandos: manejo de la metadata:
        - CREATE: Crear objetos
        - ALTER: modificar
        - DROP: eliminar

- DML: Lenguaje de manipulacion de datos.
    - Comados: para accesar y manipular datos
        - INSERT: agregar
        - UPDATE: modificar
        - DELETE: eleminar
        - TRUNCTE: eliminar todos los datos
        - SELECT: consultar datos
        

- DCL: lenguaje de control de datos:
    - Comados:
        - GRANT: otorgar permisos
        - REVOKE: quitar permisos


# Transacción
- una unica unidad de trabajo
DELETE Faturas
WHERE code_fact = 1969;

## Modelo Fisico
como sera implemtada nuestra data en el sistema


# Tipos d edatos
- Datos Numericos:
    - Enteros
    - Decimales
    - Dinero
    - Logico: 1 o 0
    - flotantes

- Fechas:
diferentes precisiones
- AAAA-MM-DD(3 bytes)

- Cadenas de caracteres
    - fijos: Char(n) ---> n bytes
    - variables: varchar(n) ----> n+2 bytes maximo

- Unicode
    - nchar(n)
    - nvarchar(n)

# Restricciones de dominio
- para los tipos de datos
- restricciones para el rango.
- No anulacion
- Unicidad

