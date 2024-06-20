import pyttsx3 as pt
import time

#initiate speech engine
engine = pt.init()
engine.setProperty("voice", 0)

def SetRate(number):
    engine.setProperty('rate', number)

def SetVolume(number):
    engine.setProperty('volume', number)

def SetVoice(Voice):
    if Voice == "Male":
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
    elif Voice == "Female":
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

def Say(string):
    print(string)
    engine.say(string)
    engine.runAndWait()

SetRate(168)
SetVolume(1.0)
SetVoice("Male")
Say("Hello, world!")

Say("No! It's goodbye world, not hello world. Please get it right!")

Say("Yo mamma so fat she played Candy Crush on her phone.")
time.sleep(1.5)
Say("Sugar Crush!")
Say(input(" Say Something >> "))

engine.save_to_file('SHUT UP!', 'python_pyttsx3_male_SHUT_UP.mp3')
engine.save_to_file('SHUT UP!', 'python_pyttsx3_male_SHUT_UP.mp2')
engine.save_to_file('SHUT UP!', 'python_pyttsx3_male_SHUT_UP.mp1')
engine.save_to_file('SHUT UP!', 'python_pyttsx3_male_SHUT_UP.wav')
engine.save_to_file('SHUT UP!', 'python_pyttsx3_male_SHUT_UP.mp4')
engine.save_to_file('SHUT UP!', 'python_pyttsx3_male_SHUT_UP.mp5')

engine.stop()

# https://pypi.org/project/pyttsx3/