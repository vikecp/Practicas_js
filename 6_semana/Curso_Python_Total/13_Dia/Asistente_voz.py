import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configuarar el micro
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar")

        # guardar lo qe escuche
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language='es-mx')

            # pudo ingresar
            print("Dijiste: " + pedido)

            # devolver a pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio elaudio
            print("Ups no entendi")

            # devolver error
            return 'Sigo esperando'

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio elaudio
            print("Ups no hay servicio")
            # devolver error
            return 'Sigo esperando'

        # error inesperado
        except:
            # prueba de que no comprendio elaudio
            print("Ups, algo a salido mal")
            # devolver error
            return 'Sigo esperando'

# transformar_audio_en_texto()


# Voces para el texto
en = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
es = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# pasar de texto a voz
def hablar(mensaje):

    # encender el moto de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', es)

    # pronunciar el msj
    engine.say(mensaje)
    engine.runAndWait()
# hablar('Hola como estas?. Esta corriendo el carro')


# informar el dia de la semana
def pedir_dia():

    # crear variable de datos de hoy
    dia = datetime.date.today()

    # crear varible para dia de la semana
    dia_semana = dia.weekday()

    # dicionario con nombres de los dias
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }
    dia_voz = f'El dia de hoy es {calendario[dia_semana]}'
    # decir el dia de la semna
    print(dia_voz)
    hablar(dia_voz)


# informar hora
def pedir_hora():
    # var con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)

    # decir hora
    hablar(hora)



# saludo inicial

def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas Noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'

    hablar(f'Hola, {momento}. soy Michi, tu asistente personal. Por favor, dime ¿Cómo te puedo ayudar?')


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro, y guardar en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google:':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'LA encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, Cualquier cosa me avisas')
            break


pedir_cosas()













# Ver opciones de voz
# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
    # print(voz)