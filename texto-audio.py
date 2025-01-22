from gtts import gTTS
import os

def texto_a_audio(texto, nombre_archivo="audio.mp3", idioma="es"):
    # Crear el objeto gTTS con el texto, el idioma y la velocidad de voz
    tts = gTTS(text=texto, lang=idioma, slow=False)

    # Guardar el archivo de audio
    tts.save(nombre_archivo)
    print(f"Archivo de audio guardado como {nombre_archivo}")

# Ejemplo de uso
texto = "Ceci, Married me please"
texto_a_audio(texto, "mi_audio.mp3", "es")

# Reproducir el archivo de audio (opcional)
# os.system("start mi_audio.mp3")  # En Windows
os.system("afplay mi_audio.mp3")  # En macOS
# os.system("mpg321 mi_audio.mp3")  # En Linux (asegúrate de tener mpg321 instalado)
