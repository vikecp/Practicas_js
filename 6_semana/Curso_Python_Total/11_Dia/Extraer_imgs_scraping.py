import bs4
import requests


resultado = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


imagenes = sopa.select('.course-box-image') # genera una lista
#print(imagenes)
contador = 1
for img in imagenes:
    contador += 1
    imagen_curso = requests.get(img['src'])
    f = open(f'mi_imagen{contador}.jpg', 'wb')
    f.write(imagen_curso.content)
    f.close()


# imagen cursos