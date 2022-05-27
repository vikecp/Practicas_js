import bs4
import requests



resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

titulo = sopa.select('title')[0].getText()

# parrafo_especial = sopa.select('p')[0].getText()


# Estraer titulos
programa_cursos = sopa.select('.main-container h3')

for h in programa_cursos:
    print(h.getText())



