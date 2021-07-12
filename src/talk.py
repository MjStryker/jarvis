
import os
import time
# import pyttsx3

from pathlib import Path
from datetime import datetime
from gtts import gTTS
from playsound import playsound

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty("voice", voices[26].id)
# # engine.setProperty("voice", "french+f6")
# engine.setProperty("rate", 130)
# engine.setProperty('volume', 1.0)


# def talk(text: str):
#     engine.say(text)
#     engine.runAndWait()


audio_rootdir = "./audio"
file_extension = ".mp3"


def create_dir_if_does_not_exist(dirpath):
    if(not os.path.isdir(dirpath)):
        print("Directory '" + dirpath + "' does not exist and will be created")
    Path(dirpath).mkdir(parents=True, exist_ok=True)


def talk(text: str):
    now = datetime.now()
    filename = "tmp_record_" + \
        now.strftime("%Y%m%d_%H%M%S_") + \
        str(int(now.timestamp())) + file_extension
    path = os.path.join(audio_rootdir, filename)

    print(filename)

    tts = gTTS(text=text, lang='fr')
    tts.save(path)

    playsound(path)

    time.sleep(0.5)
    os.remove(path)


if __name__ == "__main__":
    create_dir_if_does_not_exist(audio_rootdir)
    talk("Je n'ai pas trouvé de résultat pour votre recherche. Dois-je essayer autre chose ?")
