#A simple instagram bot with python
import instaloader

insta = instaloader.Instaloader(save_metadata=False, compress_json=False)

menu = r"""
Bienvenid@ puedes descargar contenido de Instagram... Escribe el número de la lista del menu, por el momento solo
tenemos estas opciones 

1. Descargar la foto del perfil
2. Descargar TODAS las fotos del perfil
3. Descargar las Fotos en las que haya sido etiquetado

--- Recuerda que de preferencia debe ser una cuenta pública ------
"""
print(menu)
acc = input('Ingresa el username de la cuenta de instagram: ')
entrada = int(input("Ingresa el numero de la lista del menu: "))


if entrada == 1:
    insta.download_profile(acc,  profile_pic=False,profile_pic_only=True, fast_update=False,)
if entrada == 2:
    insta.download_profile(acc, profile_pic=False, profile_pic_only=False, fast_update=False)
elif entrada == 3:
    insta.download_profile(acc, download_tagged_only=True, fast_update=False)



