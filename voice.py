import pyttsx3

def text_to_speech(text, gender,rate,volum):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]
    engine = pyttsx3.init()
    # Setting up voice rate
    engine.setProperty('rate', rate)
    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', volum)
    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)
    engine.say(text)
    engine.runAndWait()

text = 'Hello ! My name is Siddhesh.'
gender = 'Male'  # Voice assistant 
rate=200
volum=0.1
text_to_speech(text, gender,rate,volum)
