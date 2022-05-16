#p1
def potencia(n1, n2):
    potencias = n1 ** n2
    return potencias

#p2 convertir dolares a euros donde 1USD = 0.85 Euros
dolares = 50
def usd_a_eur(dolares):
    return dolares * 0.85

#p3
palabra = "vike"
def invertir_palabra(palabra):
    invertir = palabra[::-1]
    return invertir.upper()

palabra_invertida = invertir_palabra(palabra)
print(palabra_invertida)
