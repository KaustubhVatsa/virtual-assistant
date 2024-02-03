# importing text to speech module
import pyttsx3
import speech_recognition
import json
import requests

# setting up voice
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# setting the rate of speaking
engine.setProperty("rate", 170)


# print (voices[0])


# jarvis say function
def speak(audio):
    engine.say(audio)
    # after speaking we want jarvis to wait for some time
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Trying To Listen...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # controls the audio enviroment such as kitna sound mein user bolega
        audio = r.listen(source, 0, 4)  # duration of listening period

    try:
        print("Trying to Understand...")
        comm = r.recognize_google(audio, language="en-in")
        print(f"You Said :{comm}\n")
    except Exception as e:
        print("Repeat that again")
        return "None"
    return comm


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetme import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("sure sir , happy to help !")
                    break
                elif "launch" in query or "open" in query:
                    from openingapp import openapp
                    openapp(query)
                elif "google" in query:
                    from search import searchgoogle
                    searchgoogle(query)
                elif "youtube" in query :
                    from search import searchyoutube
                    searchyoutube(query)
                elif "weather" in query:
                    from weather import weather_search
                    weather_search(query)
                elif "bye" in query:
                    speak("happy to help ! have a nice day ahead !")
                    exit()


