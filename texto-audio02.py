import pyttsx3

def texto_a_audio(texto, nombre_archivo="audio.mp3"):
    # Inicializar pyttsx3
    engine = pyttsx3.init()

    # Configurar propiedades de la voz (puedes cambiar el índice para seleccionar una voz diferente)
    voces = engine.getProperty('voices')
    engine.setProperty('voice', voces[0].id)  # Cambia el índice para elegir otra voz
    
    # Configurar la velocidad de la voz
    engine.setProperty('rate', 150)  # Puedes ajustar la velocidad

    # Guardar el archivo de audio
    engine.save_to_file(texto, nombre_archivo)
    engine.runAndWait()

    print(f"Archivo de audio guardado como {nombre_archivo}")

# Ejemplo de uso
texto = "Hola, ¿cómo estás? Este es un ejemplo de conversión de texto a audio."
texto_a_audio(texto, "mi_audio02.mp3")
