# source venv/bin/activate
import os
import sys
import time
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty("voice", voices[0].id)


def talk(text: str):
    engine.say(text)
    engine.runAndWait()


talk("Bonjour Monsieur Morlet")

# while True:
# time.sleep(1)


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            # voice.adjust_for_ambient_noise(source, duration=0.2)
            # command = listener.recognize_google(voice, language="fr-FR")
            command = listener.recognize_google(voice, language="fr-FR")
            command = command.lower()
            if 'jarvis' in command:
                print("Jarvis detected !")
            return command
    except:
        pass
        # listener = sr.Recognizer()
        # continue


def run_jarvis():
    command = take_command()
    print(command)


while True:
    run_jarvis()

# if __name__ == "__main__":
#     try:
#         job()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
