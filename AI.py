import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import googlesearch
import webbrowser
import os
import random 
import sys
import pyaudio
import googletrans 


Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')
Engine.setProperty('voice', voices[0].id)

def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()


r = sr.Recognizer()
with sr.Microphone() as source:
    speak("Adjusting for background noise. One second")
    r.adjust_for_ambient_noise(source)
    speak("Say something!")
    audio = r.listen(source)

IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    speak("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    speak("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    speak("Could not request results from IBM Speech to Text service; {0}".format(e))



def wish_me():
    hours = int(datetime.datetime.now().hour)
    times = hours
    if hours >= 12:
        times = (hours - 12) 
        ampl = 'PM'
    else:
        hours = hours
        ampl = 'AM'     
    if hours < 12:
        
        speak(f'Good mornig sir time is {times} {ampl}')
    else:
        if hours >=12:
            if times ==0:
                times == 12 
            speak(f'Good afternoon sir time is {times} {ampl}')
        else:

            speak(f'Good evening sir Time is {times} {ampl}  ')
    speak('I am jarvis please tell me how can i help you sir')        

def take():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 600
        audio = r.listen(source)

    try:
        print("Recognizing sir .....")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def finder(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)



                
if __name__ == "__main__":
    wish_me()
    while True:
        query = take().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia ')
            query =query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak('According to wikipedia')
            speak(results)
        
        elif 'open Youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'play music' in query:
            path_music = 'G:\\local\\fav songs\\best'
            speak('Playing music sir')
            musics = os.listdir(path_music)
            play = random.randint(0, len(musics)-1)
            os.startfile(os.path.join(path_music, musics[play]))
        
        elif 'open chrome' in query:
            path_app = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            speak(f'opening crome sir')
            os.startfile(path_app)    
        
        elif 'open my computer' in query:
            path_pc = 'This PC'
            speak('opening my computer sir')
            os.startfile(path_pc)
        
        elif 'open code' in query :
            speak('opening code')
            pathcode = 'C:\\Users\\shivam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(pathcode)
        
        elif 'open whatsapp' in query:
            speak('Opening whatsaap')
            pahtwat = 'C:\\Users\\shivam\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(pahtwat)
        elif 'what is your name' in query:
            speak('My name is jarvis')
        
        elif 'open my drive' in query:
            speak('opening your drive sir')
            pathdri = 'F:\\'
            os.startfile(pathdri)
        elif 'how are you' in query:
            speak('I am fine sir ')

        elif 'stop' in query:
            speak('okay sir I am stoping my process')
            break
        elif 'make a text file' in query:
            speak('okay sir')
            pathtxt = 'C:\\Users\\shivam\\Documents'
            speak('In next opening you had to write only name of file not ending okay sir ')
            name = input('Enter name of your file : ') + '.txt'
            open(f'{pathtxt}\\{name}','a').close()
            speak('sir if you want to write text in your file so please tell me')
            query1 = take().lower()
            if 'write in file' in query1:
                speak('you are now in write mode')
                files = open(f'{pathtxt}\\{name}','a')
                speak('what you want to write in file please tell me')
                writer = take().lower()
                files.write(writer)
        elif 'find file' in query:
            speak('which file do you want to search sir')
        
        elif 'who is your creator' in query:
            speak('I am jarvis created by shivam singh') 
        
        
        


