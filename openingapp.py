import os
import pyautogui
import webbrowser
import pyttsx3
import subprocess
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

apps = {"command prompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"vscode","brave":"brave","valorant": "C:/Riot Games/Riot Client/RiotClientServices.exe --launch-product=valorant --launch-patchline=live"}
app_to_open = list(apps.keys())
def openapp(query):
    app = query.replace("open","")
    app = query.replace("launch","")
    try:
        speak(f"oepning{app}")
        for go_through_list in app_to_open:
            if go_through_list in query:
                if go_through_list =="valorant":
                    subprocess.Popen(apps[go_through_list],cwd="C:/Riot Games/Riot Client")
                else:
                    os.system(f"start {apps[go_through_list]}")
    except Exception as e:
        speak("failed to open app sorry for the inconvinience")






# note
# os.system: The os.system function is a simple way to execute a shell command. It runs the command in a subshell, and it's suitable for simple commands without much interaction. It waits for the command to complete before returning control to your Python script. This means that your script will be blocked until the external command finishes.
#
# Example:
#
# python
# Copy code
# os.system(f"start {apps[go_through_list]}")
# subprocess.Popen: The subprocess module provides more flexibility. subprocess.Popen allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It doesn't block your Python script; you can continue with other tasks while the external process runs. This can be useful for applications that need more control or want to perform multiple tasks simultaneously.
#
# Example:
#
# python
# Copy code
# subprocess.Popen(apps[go_through_list], cwd="C:/Riot Games/Riot Client")