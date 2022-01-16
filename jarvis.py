import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pythonproject2610@gmail.com','Psnk@2610')
    server.sendmail('pythonproject2610@gmail.com', to, content)
    server.close()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >0 and hour<12:
        speak("GOOD MORNING!")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING!")

    speak("Hello I'm Jarvis, How can I help you ?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open w3schools' in query:
            webbrowser.open('w3schools.com')

        elif 'open whatsapp' in query:
            webbrowser.open('web.whatsapp.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)
            s=random.choice(songs)
            os.startfile(os.path.join(music_dir, s))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {strTime}')
            print(strTime)
        elif 'open code' in query:
            codepath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.4\\bin\\pycharm64.exe"
            os.startfile(codepath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to='dikwalkar.prabhat5@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,your email wasn't send :(")


        elif 'exit'in query:
            quit()









