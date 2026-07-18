import speech_recognition as sr
from deep_translator import GoogleTranslator
import pyttsx3

voz = pyttsx3.init()
voz.setProperty("rate", 160)
voz.setProperty("volume", 1.0)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙 Habla ahora...")
    audio = recognizer.listen(source)

try:
    texto = recognizer.recognize_google(audio, language="es-ES")
    print("📝 Dijiste:", texto)

    idioma = input("¿A qué idioma deseas traducir? (en, fr, it, de): ")

    traduccion = GoogleTranslator(source="es", target=idioma).translate(texto)

    print("🌍 Traducción:", traduccion)

    voz.say(traduccion)
    voz.runAndWait()

except sr.UnknownValueError:
    print("❌ No se pudo entender el audio.")
    voz.say("No pude entender lo que dijiste.")
    voz.runAndWait()

except Exception as e:
    print("❌ Ocurrió un error:", e)