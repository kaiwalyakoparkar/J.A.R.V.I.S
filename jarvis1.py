import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
sr.__version__

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!! I am Jarvis,  How may I help you ?? ")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!! I am Jarvis,  How may I help you ?? ")

    else:
        speak("I am Jarvis,  How may I help you ??")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en.in')
        print(f"You Said: {query}\n")


    except Exception as e:
       # print(e)
        print("Please pardon i sir...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@via.com', 'password') 
    server.sendmail('youremail@via.com', to, content)
    server.close()  



if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

    #logic for executing tasks based on query

    if 'wikipedia' in query:
        speak('Searching i Wikipedia Database...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")




    elif 'open pintrest' in query:
        webbrowser.open("pinterest.com")


    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'play music' in query:
        music_dir = 'E:\\Kaiwalya'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\Kaiwalya.ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to client' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "clientemail@via.com"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry sir I am not able to send Email at current moment")




#pyaudio install 'https://pypi.org/project/PyAudio/#files'
#the open terminal and type 'pip install pipwin' and then let it download and install
# then type 'pipwin install pyaudio' and wait. pyaudio will be installed
#import wikipedia
#import speechRecognition


        
