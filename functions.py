import sys
import time

def line_break():
    """
    Adds a line and a blank line underneath.
    For visual pleasure.
    """
    print("__________________________________________________\n")

def close_script():
    print("\nExiting the program.")
    line_break()
    sys.exit(0)

def back_to_menu():
    line_break()
    print("Returning to menu . . .\n")
    time.sleep(2)
    print("Restarting process . . .\n")
    print("This takes only 5 seconds . . .")
    time.sleep(5)