import sys
import time
import keyboard
from colorama import Fore, Back, init


allowed_keys = ('1')

init(autoreset = True)


def line_break():
    """
    Adds a line and a blank line underneath.
    For visual pleasure.
    """
    print(Fore.CYAN + "__________________________________________________\n")

def close_script():
    print("\nExiting the program.")
    line_break()
    sys.exit(0)

def back_to_menu():
    print("Press '1' to return to the menu.")
    while True:
        event = keyboard.read_event(suppress = True)
        if event.event_type == keyboard.KEY_UP:
            choice = event.name

            if choice in allowed_keys:
                if choice == '1':
                    line_break()
                    print("Returning to menu . . .\n")
                    time.sleep(2)
                    print("Restarting process . . .\n")
                    print("This takes only 5 seconds . . .")
                    time.sleep(5)
                    break
                else:
                    break