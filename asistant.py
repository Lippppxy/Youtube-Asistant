import speech_recognition as sr
import pyttsx3
import pywhatkit

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
    except Exception as e:
        print(e)
        return ""
    return query

def greet():
    speak("Hello Alif, What song do you want to hear today?")
    
def play_song(query):
    try:
        speak("Playing " + query + " on YouTube...")
        pywhatkit.playonyt(query)
    except Exception as e:
        speak("Sorry, i cant understand")

def main():
    greet()
    while True:
        query = recognize_speech().lower()
        if "play" in query:
            query = query.replace("play", "")
            play_song(query)
        elif "goodbye" in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, i didnt understand")
    
if __name__ == '__main__':
    main()