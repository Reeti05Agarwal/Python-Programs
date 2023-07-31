import pyttsx3
import speechRecognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice", voices[0].id)
#zero is for male voice and 1 is for female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")       
    speak("I am Jarvis. PLease tell me how may i help you.")

def takeCommand():
    #it takes microphone input form user and returns string output
    r = sr.Recognitor()
    with sr.microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  #pause_threshold is the seconds of non-speaking audio before a phrase is considered completed
        audio = r.listen(source) 
 
if __name__ == "__main__":
    wishMe()
    #speak("My name is Reeti")
