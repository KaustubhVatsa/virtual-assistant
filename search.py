import webbrowser

import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser



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


query = takeCommand().lower()

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


def searchgoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google", "")
        query = query.replace("google search", "")
        speak("here is what i found on the web ")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            print(result)
            speak(result)
        except:
            speak(f"i could not find about {query} on the web")


def searchyoutube(query):
    if "youtube" in query:
        speak("searching in youtube")
        query = query.replace("find", "")
        query = query.replace("on", "")
        query = query.replace("play", "")
        query = query.replace("youtube", "")
        query = query.replace("about", "")
        query = query.replace("can you", "")
        query = query.replace("search", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak(f"here is what i found on youtube about {query}")

