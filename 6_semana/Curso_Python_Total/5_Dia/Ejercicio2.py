def eliminar_repetidas(palabra_random):
    elimina_letras_repetidas = set(palabra_random)
    return_lista = list(elimina_letras_repetidas)
    return_lista.sort()
    print(return_lista)

eliminar_repetidas("entretenido")
