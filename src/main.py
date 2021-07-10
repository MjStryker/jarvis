# source venv/bin/activate
import os
import sys
import time
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()


def job():
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(language="fr-FR")
                text = text.lower()

                print(f"You said: {text}")

        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            continue

    # time.sleep(1)


if __name__ == "__main__":
    try:
        job()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
