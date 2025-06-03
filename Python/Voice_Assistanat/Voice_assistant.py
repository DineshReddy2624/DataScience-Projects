import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnKownError:
            print("Not Understood")
def speech(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':
    
    if "hey jimmy" in sptext().lower():
        data_value=sptext().lower()
        while True:
            if "your name" in data_value:
                name="my name is Jimmy"
                speech(name)
            elif "time" in data_value:
                time=datetime.datetime.now().strftime("%I%M%p")
                speech(time)
            elif "linkedin" in data_value:
                webbrowser.open("https://www.linkedin.com/in/dinesh-reddy-kommi-reddy-639878305/")
            elif "jokes" in data_value:
                Jokes=pyjokes.get_joke(language="en")
                print(Jokes)
                speech(Jokes)
            elif "play song" in data_value:
                add=  "D:\music"
                list_song=os.listdir(add)
                print(list_song, end="\n")
                os.startfile(os.path.join(add,list_song[2]))
            elif "exit" in data_value:
                speech("It is Nice speaking to u Thank you....!")
                break      
    else:
        print("Thank you..!")
