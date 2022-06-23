import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',200)

def say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 200)
    print(f"Nello: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")