import speech_recognition as sr
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=5)
        text = ""
        try:
            text = r.recognize_google(audio)
            print(text)
        except Exception as e:
            print("Exception: " + str(e))
listen()