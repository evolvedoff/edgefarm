import pyautogui
import time
import random
import keyboard
import sys

def generate_random_letters():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choices(letters, k=4))

def search_edge(repeats, custom):
    pyautogui.hotkey('ctrl', 'e')
    if custom:
        pyautogui.typewrite(custom)
    else:
        random_letters = generate_random_letters()
        pyautogui.typewrite(random_letters + str(repeats))
    pyautogui.press('enter')

debouncerun = True

repeats = 30

def run():  
    global debouncerun
    global repeats
    if debouncerun and repeats >= 0:
            debouncerun = not debouncerun
            search_edge(repeats, custom=0)
            time.sleep(random.randint(90,110) / 10)
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
