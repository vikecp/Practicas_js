def pedirnumero():
    while True:
        try:
            num = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f'Ingresaste el numero {num}')
            break
    print("Gracias")

pedirnumero()