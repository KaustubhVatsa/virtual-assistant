import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import json
import requests



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

def extract_city_name(query):
    # Split the query into words
    words = query.split()

    # Look for the index of the keyword "in"
    try:
        index_of_in = words.index("in")
    except ValueError:
        # If "in" is not found, return None or handle it as per your requirement
        from getgps import currentloc
        return currentloc()

    # Extract the city name that follows "in"
    city_name = " ".join(words[index_of_in + 1:])

    return city_name
def weather_search(query):
    if "weather" in query :
        cityname = extract_city_name(query)
        apikey = "your_api_key(openweather)"
        base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        completeurl = base_url + cityname + "&appid=" + apikey
        response = requests.get(completeurl)
        if response.status_code == 200:
            weather_data = response.json()

            # Extracting temperature values and converting them to Celsius
            temp_max_celsius = round(weather_data['main']['temp_max'] - 273.15, 2)
            temp_min_celsius = round(weather_data['main']['temp_min'] - 273.15, 2)
            feels_like_celsius = round(weather_data['main']['feels_like'] - 273.15, 2)
            speak(f"current temperature in {cityname} feels like {feels_like_celsius} degree celcius ")
        else:
            speak("sorry i could not understand")
