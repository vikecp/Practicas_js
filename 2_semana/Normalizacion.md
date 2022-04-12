# Normalización
- Poner en order lo que no estaba
- Ordenar, estandarizar, mejorar nuestras relaciones.
- Que ordenar?----La redundancia.

**Proceso secuencial, ciclico y repetitivo a todas y cada una de las entidades del modelo y se aplica un conjunto de reglas bien definidas**

### Anomalias de insercion
- no se puede insertar datos sin la presencia de otros atributos.
- anomalia de modificación
- anomalia de eliminación

# Formas Normales
1. Primera Forma Normal(1NF):
    - no debe haber duplad repetidas
    - Existencia de una llave primaria
    - atributos atomicos

    **Una relacion esta en (1NF) si, y solo si, no tiene grupos repetitivos**

2. Segunda Forma Normal

**Una relación esta en (1NF) si, y solo si:**
    1. Esta en 1NF
    2. Todos los atributos dependen de la llave primaria completa
        - Ningun atributo depende unicamente de una parte de la llave primaria.

    No hay una llave primaria compuesta

3. Tercera Forma Normal
**Una relación esta en (3NF) si, y solo si:**
    1. Esta en 2NF
    2. Ningun atributo "no determinante" depende transitivamente de la llave primaria

4. Cuarta Forma Normal 

# Normalización Superior
- Aun despues de la 3NF puede haber redundancia

