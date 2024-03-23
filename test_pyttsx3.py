import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate', 110)
for i in range (5):
    engine.say('test')
engine.runAndWait()