#p1
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

# 2 obtner el 2 item de la lista points2
mi_dict = {
    "valores_1":{"v1":3,"v2":6},
    "puntos":{"points1":9,"points2":[10,300,15]}
}
print(mi_dict["puntos"]["points2"][1])


# P3
mi_dic = {
    "nombre":"Karen",
    "apellido":"Jurgens",
    "edad":35,
    "ocupacion":"Periodista"
}
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"