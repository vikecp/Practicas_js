def devolver_distintos(n1,n2,n3):
    suma = n1 + n2 +n3
    lista = [n1,n2,n3]
    mayor = max(lista)
    menor = min(lista)
    prom = suma / 3
    if suma > 15:
        print(mayor)
    elif suma < 10:
        print(menor)
    else:
        print(prom)


devolver_distintos(8,1,0)
