import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import re
import subprocess
import requests


#sapi5 is one of the microsoft api it will provide me with the necessary voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#here i had set the voice 0 for boy 1 for girl
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning , Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ,Sir")

    else:
        speak("Good Evening ,Sir")

    speak("Ignitia here , Please tell me how may i help you ?")
    
    

def takeCommand():
    #it takes input from user and return string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        #ye jo print(e) hai ye mera error show kreaga ki kya error aa raha h
        #filal isse comment kr dia h maine
        print('Say that again please...')
        return "None"

    return query

def sendmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password here')
    server.sendmail('youremail@gmail.com', to ,content)
    server.close()

def interact():
    speak("I will love to interact with you Sir. So how are you?")
    while True:
        query = takeCommand().lower()

        if 'good' in query:
            speak("That's great sir")

        elif 'about me' in query:
            speak(info)

        elif 'family' in query:
            speak(info1)

        elif 'who are' in query:
            speak("I am Ignitia ... i am an A I assistant")
    
        elif 'add info' in query:
            info['added data'] = takeCommand()
            speak("You added")
            speak(info["added data"])

        elif 'exit' in query:
            speak("exiting interaction mode")
            return    

info1 = dict({'Father name' : "your-father-name",
                'Mother name' : "your-mother-name",
                'Address': "your-address"

                })

info = dict({'Your name': "kanupriya Malik" ,
            'Age' :21,
            'Favourite Color' :"White ",
            'Favourite food' :"Mexican , Indian and chinese",
            'Relationship status' : "Unknown to me"})

if __name__ == "__main__":
    
    wishMe()

    while True:

        query = takeCommand().lower()
       
        #logics for executing tasks based on queries

        #logic to search for anything on wikipedia
        if 'search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            speak(results)

        #logic for opening a particular website
        elif 'open' in query:
            w_site = re.search('open (.+)',query)
            if w_site:
                domain = w_site.group(1)+'.com'
                print(domain)
                url = 'https://www.' + domain 
                webbrowser.open(url)
                speak('The website has been opened sir , have a look')
            else:
                pass

        elif 'interact with me' in query:
            interact()

        

        elif 'play music' in query:
            music_di = 'C:\\Users\\Kanupriya\\Music\\bolywood'  #Add your music files path here
            songs = os.listdir(music_di)
            d=random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_di,d))
        
        elif 'note' in query:
            fd = "data.txt"
            file = open(fd ,'w')
            speak("What do you want me to record into it , Sir")
            try:
                data = takeCommand()
                file.write(data)
                file.close()
                speak('Your note has been recorded succesfully , Sir')
                
            except Exception as e:
                speak("error occured")
                print(e)
        #to tell what was the note
        elif 'data' in query:
            fd = "data.txt"
            file = open(fd ,'r')
            ram = file.read()
            speak(f"The data was : {ram}")

        elif 'the time' in query:
            timeis = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {timeis}")

        elif 'open code' in query:
            vcode = 'C:\\Users\\Kanupriya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'   #Add your music files path here
            os.startfile(vcode)

        elif 'email to xyz' in query:
            #gmail ki settings mai ja kr unknown apps ko allow krna
            #hoga tbhi mail ja payegi
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "reciver-mail@gmail.com"
                sendmail(to,content)
                speak('Email has been sent.')
            except Exception as e:
                print(e)
                speak("Sorry sir mail has not been sent")

        elif 'exit' in query:
            speak("Have a nice day sir i will meet you soon")
            exit()
        
        elif 'shutdown' in query:
            speak("Do you really want to shutdown the PC")
            input = takeCommand().lower()
            if 'yes' in query:
                os.system("shutdown /s /t 1")
            else:
                speak('Thats a good choice.')

        elif 'restart' in query:
            speak("Do you really want to shutdown the PC sir")
            input = takeCommand().lower()
            if 'yes' in query:
                os.system("shutdown /r /t 1")
            else:
                speak('Thats a good choice.')  
      
        elif 'locate' in query:
            w_loc = re.search('locate (.+)',query)
            if w_loc:
                place = w_loc.group(1)
                print(place)
                url = 'https://www.google.com/maps/place/' + place 
                webbrowser.open(url)
                speak(f'{place} has been located on map sir , have a look')
            else:
                pass
            
        


