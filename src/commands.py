import config
import locale

from datetime import datetime
from talk import talk


locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

assistant_name = config.personal_assistant_name.lower()


def execute_command(command: str):
    command = command.lower()
    now = datetime.now()
    date = now.strftime("%A %d %B %Y")
    hour = now.strftime("%H:%M")

    if ("lisa" in command):
        talk("Elle prépare sa valise pour les vacances :)")
    elif("jeanne" in command):
        talk("Elle fait du café, hahaha, mdr")
    elif("bonjour" in command):
        talk("Bonjour")
    elif("jour" in command):
        talk(f"Nous somme le {date}")
    elif("heure" in command):
        talk(f"Il est {hour}")
    else:
        print("Unknown command...")
        talk("Je n'ai pas compris...")


if __name__ == "__main__":
    print()
    # execute_command("Bonjour")
    # execute_command(f"on est quel jour {assistant_name} ?")
    # execute_command(f"qu'elle heure est-il {assistant_name} ?")
