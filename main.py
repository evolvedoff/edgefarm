import pyautogui
import time
import random
import keyboard
import sys
from wonderwords import RandomWord as r

def generate_random_word():
    return r().word()

def search_edge(repeats, custom):
    pyautogui.hotkey('ctrl', 'e')
    if custom:
        pyautogui.typewrite(custom)
    else:
        random_letters = generate_random_word()
        pyautogui.typewrite(random_letters + str(repeats))
    time.sleep(0.1)
    pyautogui.press('enter')

debouncerun = True

repeats = 30

def run():  
    global debouncerun
    global repeats
    if debouncerun and repeats >= 0:
            debouncerun = not debouncerun
            search_edge(repeats, custom=0)
            time.sleep(random.randint(900, 1100) / 100)
            repeats -= 1
            debouncerun = not debouncerun
    elif repeats < 0:
        search_edge(0, "Script finished")
        print("Script finished")
        sys.exit(0)

if __name__ == "__main__":
    running = False
    debounce = True
    
    print("Press F1 to start/stop the script.")

    while True:
        if keyboard.is_pressed('F1') & debounce:
            running = not running
            debounce = not debounce
            
            if running:
                print("Script started")
                search_edge(0, "Script started")
            else:
                print("Script stopped")
                search_edge(0, "Script stopped")
                time.sleep(2)

            time.sleep(0.1)
            debounce = not debounce
        if running:
             run()
