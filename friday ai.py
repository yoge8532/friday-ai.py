import pyttsx3
import webbrowser
import os
import speech_recognition as sr

engine = pyttsx3.init()
text = "hey sir my name is friday \nhow may i help you"
engine.say(text)
engine.runAndWait()

def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results from the service."

if __name__ == "__main__":
    while True:
        command = listen_and_recognize()
        print(f"You said: {command}")
        if "stop" in command.lower():
            break
        if "open youtube" in command.lower():
            print("Opening YouTube...")
            text1 = "opening youtube"
            engine.say(text1)
            engine.runAndWait()
            webbrowser.open("https://www.youtube.com")
            break  # Remove this if you want to keep listening for more commands

        if "open google map" in command.lower():
            print("openig google map....")
            text2 = "google map"
            engine.say(text2)
            engine.runAndWait()
            webbrowser.open("https://maps.google.com/")
            break

        if "open google" in command.lower():
            print("opening google...")
            text3 = "opening google"
            engine.say(text3)
            engine.runAndWait()
            webbrowser.open("https://www.google.com/?authuser=0")
            break
    
        if"open gmail" in command.lower():
            print("opening gmail")
            text4 = "opening gmail"
            engine.say(text4)
            engine.runAndWait()
            webbrowser.open("https://accounts.google.com/b/0/AddMailService")
            break
        
        if "open vpn gate" in command.lower():
            print("opening vpngate.....")
            text5 = "opening vpn gate"
            engine.say(text5)
            engine.runAndWait()
            webbrowser.open("https://www.vpngate.net/")
            break
        
        if "open google account" in command.lower():
            print("opening your google account...")
            text6 = "opening your google account"
            engine.say(text6)
            engine.runAndWait()
            webbrowser.open("https://myaccount.google.com/?utm_source=OGB&utm_medium=app&authuser=0")
            break

        if "open google news" in command.lower():
            print("opening google news...")
            text7 = "opening google news"
            engine.say(text7)
            engine.runAndWait()
            webbrowser.open("https://news.google.com/?authuser=0")
            break

        if "open google meet" in command.lower():
            print("opening google meet...")
            text8 = "opening google meet"
            engine.say(text8)
            engine.runAndWait()
            webbrowser.open("https://meet.google.com/?hs=197&authuser=0")
            break

        if "open contact" in command.lower():
            print("opening your contacts...")
            text9 = "opening my contacts"
            engine.say(text9)
            engine.runAndWait()
            webbrowser.open("https://contacts.google.com/?authuser=0")
            break

        if "open drive" in command.lower():
            print("opening your drive...")
            text10 = "opening your drive"
            engine.say(text10)
            engine.runAndWait()
            webbrowser.open("https://drive.google.com/?authuser=0")
            break

        if "open google translator" in command.lower():
            print("opening translator...")
            text11 = "opening google translator"
            engine.say(text11)
            engine.runAndWait()
            webbrowser.open("https://translate.google.com/?authuser=0")
            break

        if "stop friday" in command.lower():
            print("Stopping speech recognition.")
            text12 = "stoping speech recognition"
            engine.say(text12)
            engine.runAndWait()
            break




        
        


