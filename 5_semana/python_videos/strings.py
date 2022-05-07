myStr = "Viike"

#imprimir una variable 
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))

# print(dir(myStr)) ----> metodos que tiene
# Poner en Mays
print(myStr.upper())
myStr.lower()
myStr.capitalize()
print(myStr.replace("Hi", "Bye"))

#cotar cuantas veces tengo cierto caracter
myStr.count('l')
#Si el texto escrito inicia con ciert palabra
myStr.startswith("Hello") # False
myStr.endswith("word")

# divide cuando hay un espcio
myStr.split('')

# buscar en que posicion esta esa letra
myStr.find('o')

# longitud
len(myStr)

# Saber indice
myStr.index('e')

# si es numerico
myStr.isnumeric() # false
myStr.isalpha()

# ver el valor
myStr[0]
myStr[-1]