import pyttsx3
voz = pyttsx3.init()

voz.setProperty("rate", 150)
voz.setProperty("volume", 1.0)

texto = input("Escribe un mensaje: ")

voz.say(texto)
voz.runAndWait()