# Aplicación de Síntesis de Voz

## Descripción

Este proyecto fue desarrollado en Python utilizando la biblioteca `pyttsx3`.

La aplicación permite convertir texto en voz mediante síntesis de voz. Además, incluye una versión mejorada que escucha la voz del usuario, la convierte en texto, la traduce al idioma elegido y reproduce la traducción en voz alta.

## Tecnologías utilizadas

- Python 3
- SpeechRecognition
- deep-translator
- pyttsx3
- PyAudio

## Archivos

- `main.py`: aplicación básica de síntesis de voz.
- `mejorado.py`: aplicación mejorada que reconoce la voz del usuario, traduce el mensaje y reproduce la traducción mediante síntesis de voz.

## Instalación

Instalar las dependencias:

```bash
pip install SpeechRecognition
pip install deep-translator
pip install pyttsx3
pip install pyaudio
```

## Ejecución

Versión básica:

```bash
python main.py
```

Versión mejorada:

```bash
python mejorado.py
```

## Funcionamiento

1. El usuario habla por el micrófono.
2. El programa reconoce el mensaje.
3. Se elige el idioma de destino.
4. El texto se traduce automáticamente.
5. La traducción se reproduce en voz alta.

## Autor

Sara Drago Ponzoni