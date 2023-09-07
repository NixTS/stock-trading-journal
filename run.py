from functions import line_break
from sheet_data import *
from pynput.keyboard import Listener
from pynput import keyboard

allowed_keys = {'1', '2', '3', keyboard.Key.esc}

import subprocess

from colorama import just_fix_windows_console
just_fix_windows_console()

def start():
    """
    Starting point
    Prints a message to the UI to select options:
    1: Input stock trading data
    2: Show past trades
    3: Get statistics 
    """

    print("Welcome to your Stock Trading Journal")
    print("Please press one of the following buttons on your keyboard to continue:\n")
    print("'1' to input your stock trading data.")
    print("'2' to see your past journal entries.")
    print("'3' to see your past trading statistics.\n")

def on_key_press(key):
    try:
        if key.char in allowed_keys:
            if key.char == '1':
                subprocess.run(["python", "input_stock_data.py"])
            elif key.char == '2':
                subprocess.run(["python", "show_past_trades.py"])
            elif key.char == '3':
                subprocess.run(["python", "get_statistics.py"])
    except AttributeError:
        # Handle 'Esc' key
        if key == keyboard.Key.esc:
            print("\nExiting the program.")
            quit()

start()

with Listener(on_press=on_key_press) as listener:
    print("Press 1, 2, or 3 to select an option (Esc to exit).")
    listener.join()