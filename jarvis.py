import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from playsound import playsound
cnum = random.randint(0,2)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            speak("Good Morning")
        elif hour>=12 and hour<=18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")  
        speak("welcome back what we do next..")
def takeCommand():
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please:")
        return "None"
    return query   

if __name__ == "__main__":
    wishme()
    # takeCommand()
    while True:
            
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 8)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
             music_dir = 'E:\Music'
             songs = os.listdir(music_dir)
            #  print(songs)
             os.startfile(os.path.join(music_dir, songs[cnum]))
        elif 'open code' in query:
            Path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)
        elif 'open blender' in query:
            Path2 = "C:\\Program Files\\Blender Foundation\\Blender 3.2\\blender-launcher.exe"
            os.startfile(Path2)
        # elif 'open notepad' in query:
        #     Path3= '%windir%\\system32\\notepad.exe'
            # os.startfile(Path3)
        elif 'open chrome' in query:
            Path4 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(Path4)
        elif 'open firefox' in query:
            Path5 = "C:\\Program Files (x86)\Mozilla Firefox\\firefox.exe"
            os.startfile(Path5)
        elif 'open ms word' in query:
            Path6 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(Path6)
        elif 'open ms excel' in query:
            Path7 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(Path7)
        elif 'open powerpoint' in query:
            Path8 = "C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE"
            os.startfile(Path8)
        elif 'open edge browser' in query:
            Path9 = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" 
            os.startfile(Path9)
        elif 'great jarvis' in query:
            speak("Thank you sir! i think you are a genius. sir")
        elif 'amazing jarvis' in query:
            speak("It's nothing sir!")
        elif 'what i do' in query:
            speak("You promises sometimes ago and says you will try Hacking, typing, solving math questions and other things")
        elif 'who are you' in query:
            speak("I am jarvis a virtual assistance of Saksham Mishra")
        elif 'what is your name' in query:
            speak("I am jarvis sir!")
