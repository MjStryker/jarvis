# source venv/bin/activate
import os
import sys
import time
import speech_recognition as sr
import config

from datetime import datetime

from commands import execute_command

listener = sr.Recognizer()
assistant_name = config.personal_assistant_name.lower()


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occurred, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit=5)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(
            audio, language="fr-FR").lower()
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "..."
        # response["error"] = "Unable to recognize speech"

    return response


def take_command(recognizer, microphone):
    speech = recognize_speech_from_mic(recognizer, microphone)

    # if there was an error
    if speech["error"]:
        print("ERROR: {}".format(speech["error"]))

    # show the user the transcription
    command = speech["transcription"]
    print(f"You said: {command}")

    if (command is not None and assistant_name in command):
        command = command.replace(assistant_name, "").strip()
        print(f"Your command: {command}")
        execute_command(command)


def run_assistant():
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        try:
            take_command(recognizer, microphone)
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)


if __name__ == "__main__":
    # print()
    run_assistant()
    # command = "Quelle heure est-il Friday ?".lower()
    # if (assistant_name in command):
    #     command = command.replace(assistant_name, "").strip()
    #     print(f"Your command: {command}")
    #     execute_command(command)
