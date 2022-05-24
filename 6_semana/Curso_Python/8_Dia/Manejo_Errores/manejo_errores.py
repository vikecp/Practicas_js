def suma():
    n1 = int(input("num1: "))
    n2 = int(input("num2: "))
    print(n1 +n2)



try:
    suma()
    # codigo que queremos probar
except TypeError:
    print("Algo no ha salido bien porque estan concatenando dos tipos distintos ")
    #codigo a ejecutar si hay un error
except ValueError:
    print("Ese no es un numero")
else:
    print("Hiciste todo bien")
    #codigo a ejecutar si
finally:
    print("Eso fue todo")
    #se ejecutara pase lo que pase


