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
    """
    line_break()
    print("Welcome to your Stock Trading Journal!\n")
    print("Please press one of the following buttons on your keyboard to continue:\n")
    print("'1' to input your stock trading data.")
    print("'2' to display your journal entries.")
    print("'3' to display your trading statistics.\n")
    print("'ESC' to exit the program.")

def on_key_press(key):
    """
    Handles key presses to 
    1: Input stock trading data to journal
    2: Display trading journal
    3: Display trading statistics 
    ESC: to exit the program
    """
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
            line_break()
            quit()

start()

with Listener(on_press=on_key_press) as listener:
    listener.join()