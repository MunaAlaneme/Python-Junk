import speech_recognition as sr # initiate speech recognition
import webbrowser as web

r = sr.Recognizer() # initiate recognizer

while(1):
    try:
        with sr.Microphone() as source: # initiate microphone
            print("Listening...")
            audio = r.listen(source) # listen for audio
            mytext = sr.recognize_google(audio)
            print(mytext)
            web.open_new("https://www.google.com/" + mytext)
            print(audio)
            print("Done!")
    except sr.connection_error:
        print("Error: Unable to connect to Google.")
        print("Google speech recognition requires an internet connection.")
        print("Please try again when you have an internet connection.")
    except sr.UnknownValueError:
        print("Sorry, but I don't understand what you said. Please try again.")
