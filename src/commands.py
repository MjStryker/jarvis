from datetime import datetime

from main import talk

import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')


def execute_command(command: str):
    command = command.lower()
    now = datetime.now()
    date = now.strftime("%A %d %B %Y")
    hour = now.strftime("%H:%M")

    if("jour" in command):
        print(date)
        talk(f"Nous somme le {date}")
    elif("heure" in command):
        talk(f"Il est {hour}")
    else:
        print("...")


if __name__ == "__main__":
    execute_command("on est quel jour Jarvis ?")
    # execute_command("qu'elle heure est-il Jarvis ?")