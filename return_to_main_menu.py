import keyboard
from run import main

def back_to_main_menu():
    esc_pressed = False  # Track if 'Esc' has been pressed
    
    while True:
        if keyboard.is_pressed('esc'):
            if not esc_pressed:
                print("\nyou pressed Esc, so exiting...")
                esc_pressed = True
                main()
        else:
            esc_pressed = False

if __name__ == "__main__":
    back_to_main_menu()