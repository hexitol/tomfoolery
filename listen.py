import speech_recognition as sr

def Listen():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening to you...")
        r.pause_threshold = 1
        audio = r.listen(source,0,2)

    try:
        print("Processing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You: {query}")

    except:
        return ""

    query = str(query)
    return query.lower()        

Listen()