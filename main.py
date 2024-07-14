import speech_recognition as sr
import webbrowser
import pyttsx3
import musicliberary as m
import requests
import clint as helper
import gtts as g
#pip install pocketsphinx

end = ["finish","end","exit","break"]

r = sr.Recognizer()
engine = pyttsx3.init()

import pygame
import os

# Replace 'your_api_key_here' with your actual API key
newsapi = 'your_api_key_here'

def speak(text):
    tts = g.gTTS(text=text, lang='en')
    filename = f"temp.mp3"
    tts.save(filename)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove(filename)


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Intializing jarvis.......")
    while True:
        # Use the microphone as the source
        # r = sr.Recognizer()
        
        print("recognising....")
        # Recognize speech using Google Web Speech API
        try:
            with sr.Microphone() as source:
                print("Adjusting for ambient noise...")
                r.adjust_for_ambient_noise(source)
                print("Say something!")
                audio = r.listen(source,timeout=1,phrase_time_limit=2)


            word = r.recognize_google(audio)
            if(word.lower() in end):
                speak("Exiting.....")
                exit()

            #if word jarvis come in word then start taking command from user
            if(word.lower() == "jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:

                    #check for any extra voice and clear it
                    print("Adjusting for ambient noise...")
                    r.adjust_for_ambient_noise(source)

                    #Take input voice msg or commanf from user
                    print("jarvis Active....")
                    audio = r.listen(source,timeout=1,phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print(command)

                    #a condition to exit the programm by some keywords
                    if(command.lower() in end):
                        speak("Exiting.....")
                        exit()

                #funcion to excute all command given to the jarvis
                helper.processCommand(command)
            
            elif(word.lower().startswith("jarvis")):
                speak("executing your program")
                command = word[7:]
                helper.processCommand(command)

        #check i there is some error or not listen anything
        except Exception as e:
            print("Error; {0}".format(e))
