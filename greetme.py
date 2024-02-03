#importing text to speech module 
import pyttsx3
import datetime
#setting up voice
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
#setting the rate of speaking 
engine.setProperty("rate",170)
# print (voices[0])


#jarvis say function 
def speak(audio):
    engine.say(audio)
    #after speaking we want jarvis to wait for some time 
    engine.runAndWait()

def greetMe():
    #our voice assistant will greet us based on the  time of the day
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,Sir")
    elif hour>12 and hour<18:
        speak("good afternoon,Sir")
    else:
        speak("good evening,sir")
    speak("how may i assist you today?")
    