#p1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(paises,capitales))
for pais, capital in combinados:
    print(f"La capital de {pais} es {capital}")

#p2
marcas = ["puma", "iphone","dell"]
productos = ["Tenis", "Celular", "laptop"]
mi_zip = list(zip(marcas,productos))
print(mi_zip)

#p3
num_es = ["uno","dos","tres","cuatro","cinco"]
num_port = ["um","dois","três","quatro","cinco"]
num_en = ["one","two","three","four","five"]

numeros = list(zip(num_es,num_port,num_en))
print(numeros)