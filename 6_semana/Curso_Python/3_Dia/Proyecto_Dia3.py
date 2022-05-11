# Programa un analizador de texto
app = """
-----------Analizador de texto------------- 
Las 3 Letras son para saber cuántas veces aparecen en el texto
"""
print(app)
# entrada
texto = input("Ingresa el texto que quieras analizar : ")
letras = input("Ingresa 3 letras a tu eleccion (debes ingresarlas con un espacio): ")

# convertir a lista y a minusculas
letras_minus = letras.lower().split()
tex_minus = texto.lower()

# Cuantas veces aparece cada letra
contar_letra1 = tex_minus.count(letras_minus[0])
contar_letra2 = tex_minus.count(letras_minus[1])
contar_letra3 = tex_minus.count(letras_minus[2])

# ver cuantas palabras hay en total
texto_a_lista = tex_minus.split()
contar_palabras = len(texto_a_lista)

# cual es la primera y la ultima letra
primera_letra = tex_minus[0]
ultima_letra = tex_minus[-1]

# texto en orden invertido
texto_invertido = texto[::-1]

#Si existe python?
buscar_python = "python" in tex_minus
dicc = {
    True: "si",
    False: "no"
}


print(f"""
Analizando tu texto:
1.- La letra {letras_minus[0]} aparece {contar_letra1} veces \n
2.- La letra {letras_minus[1]} aparece {contar_letra2} veces \n
3.- La letra {letras_minus[2]} aparece {contar_letra3} veces \n
4.- EL texto tiene {contar_palabras} palabras \n
5.- La Primera letra del texto es: {primera_letra} \n
6.- La ultima letra del texto es: {ultima_letra} \n
7.- Tu texto invertido se ve asi: {texto_invertido}
8.- La palabra "Python" {dicc[buscar_python]} se encuentra en el texto \n
Eso es todo el analisis de tu texto, Gracias!!!
""")

