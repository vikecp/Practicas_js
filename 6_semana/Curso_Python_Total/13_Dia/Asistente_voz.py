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


transformar_audio_en_texto()

