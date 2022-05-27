import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1, 11):
    print(url_base.format(n))



# estraer 1 libro solo que tenga 4 o mas estrellas

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod') # crea una lista

ejemplo = libros[0].select('.a')[1]['title']

