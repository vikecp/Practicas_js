# p1
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#')
print(texto)

#p2 metodo insert
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

#p3 verifica que cada set tenga elementos diferentes si son iguales es False
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv) # resp: False 
