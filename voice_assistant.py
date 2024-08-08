import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

import speech_recognition as sr

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results; check your network connection")

def speechtex(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    
    if  'hello umar' in sptext():
        while True:
                data1 = sptext().lower()
                if 'your name' in data1:
                    name = 'my name is umar'
                    speechtex(name)

                elif 'old are you' in data1:
                    age = 'i am twenty years old'
                    speechtex(age)

                elif 'time' in data1:
                    time = datetime.datetime.now().strftime("%I%Mp")
                    speechtex(time)

                elif 'yutube' in data1:
                    webbrowser.open('https://www.yutube.com')

                elif 'web' in data1:
                    webbrowser.open("Enter the name of your favourite web ")

                elif 'jokes' in data1:
                    joke_1 = pyjokes.get_joke(language='en',category='neutral')
                    print(joke_1)
                    speechtex(joke_1)

                elif 'play song' in data1:
                    add = 'D:/favourite songs/song'
                    listsong = os.listdir(add)
                    os.startfile(os.path.join(add.listsong[0]))

                elif 'exit' in data1:
                    speechtex("Thank you")
                break
    else:
        print("Thanks Assistant")

