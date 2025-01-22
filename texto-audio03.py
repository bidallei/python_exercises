from TTS.api import TTS

# Lista de modelos disponibles
print(TTS.list_models())

# Selecciona un modelo
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True)

# Convierte texto a audio y guarda el archivo
texto = "Hola, este es un ejemplo utilizando TTS."
tts.tts_to_file(text=texto, file_path="mi_audio_tts.wav")