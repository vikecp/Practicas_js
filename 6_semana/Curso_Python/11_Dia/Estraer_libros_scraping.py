import bs4
import requests

# crear url sin num de pag
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas

for pagina in range(1, 50):

    # crear sopa para cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los sibros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # checar si tienen 4 o mas estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) == 0:

            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver los libros sacados
for t in titulos_rating_alto:
    print(t)