#!/usr/bin/env python3
from os import name
from pip import main
import datetime
import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
    r.pause_threshold=1
    audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print("User-said",query)
    except Exception as e:
        # print(e)
        print("Say that again")
        
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour <18:
        speak("GOOD AFTRENOON")
    else:
        speak("Good Evening")
    speak("Welcome sir . How can I help You ")


if __name__ == '__main__':
    wishme()
    takecommand()