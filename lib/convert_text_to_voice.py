import pyttsx3


def convert_text_to_voice(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125) # Exemplo: 125% da velocidade normal
    engine.setProperty('volume', 1) # Define o valor do volume (entre 0 e 1)
    engine.say(text)
    engine.runAndWait()
