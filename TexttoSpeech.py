import pyttsx3 #To install module enter pip install pyttsx3 in terminal

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #For female voice enter 1.
engine.setProperty('rate', 150)           #To make the voice slow and fast decrease and increase the values here.



def speak(text):
    engine.say(text)

speak("ENTER YOUR TEXT HERE TO SPEAK")  #Here you can enter any text, it will speak the entered text.
