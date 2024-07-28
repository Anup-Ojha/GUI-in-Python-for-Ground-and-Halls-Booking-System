import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from requests import get
import pywhatkit.remotekit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio) -> object:
    engine.say(audio)
    engine.runAndWait()
    return object

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        speak("I am Liira Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresholpipd = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
        return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikip"
                  "edia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Sir, what should i search on google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'open yahoo' in query:
            webbrowser.open("yahoo.com")
        elif 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open chrome' in query:
            npath = "C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'play music' in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
        elif "play songs in youtube" in query:
            pywhatkit.playonyt("Bapu Zammindar")
        elif "no thanks" in query:
            speak("Thank you for using me, Have a Good Day!")
            sys.exit()
        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is{strTime}")
        elif "activate how to do mode" in query:

            from pywikihow import search_wikihow

            speak("How to do mode is activated. please tell me what you want to know?")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
            speak("Do you have any other work?")