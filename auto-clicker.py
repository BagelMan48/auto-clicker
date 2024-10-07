#OH YEA BABY ITS FINALLY FINISHED!!!

from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode
import time
import threading

mouse_controller = Controller()
keyboard_controller = keyboard.Controller()
clickButton = Button.left


def spamFrequency():
    spamFreq = float(input("How many clicks per second? "))
    try:
        spamFreqCheck = 1/spamFreq
        if (spamFreqCheck < 0):
            print("You can't spam click a negative amount of times per second")
            while (spamFreq <= 0):
                spamFreq = float(input("Please enter a number greater than 0: "))

    except ZeroDivisionError:
        print("You can't spam click 0 times per second")
        while (spamFreq <= 0):
            spamFreq = float(input("Please enter a number greater than 0: "))

    spamFreq = 1/spamFreq
    print(f"Fun fact: you will be clicking once every {spamFreq:.3f} seconds.")
    
    return spamFreq


global program_running
program_running = True


def on_press(key):
    global program_running
    global keyToggleSpamKeyCode
    global spamFreq
    global spamClick
    global counter

    if key == keyToggleSpamKeyCode:
        spamClick = not spamClick

        if spamClick:
            print("You are spam clicking.")
            
        elif (not spamClick):
            print("You have stopped spam clicking.") 

    elif key == keyboard.Key.esc:
        print("Program stopping")
        program_running = False
        print(f"You clicked {counter} times in total.")
        return False
    

def spamClicking(spamFreq):
    global program_running
    global spamClick
    global counter
    counter = 0

    while program_running:
        while spamClick:
            mouse_controller.click(clickButton, 1)
            counter += 1
            time.sleep(spamFreq)
        time.sleep(0) # need this in order for program_running loop to work if spamClick is initially False


def autoClicker(spamFreq, keyToggleSpam):
    global keyToggleSpamKeyCode
    keyToggleSpamKeyCode = KeyCode(char=keyToggleSpam)

    global x
    spamClick_thread = threading.Thread(target=spamClicking, args=(spamFreq,), daemon=True)
    spamClick_thread.start()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    keyToggleSpam = input("What key do you want to toggle spam clicking? ").lower()
    while (len(keyToggleSpam) != 1):
        keyToggleSpam = input("Please enter a single character: ")

    global spamFreq
    spamFreq = spamFrequency()

    global spamClick
    spamClick = False
    
    startSpam = input("Do you want to start spam clicking? (y/n) ")
    while (startSpam.lower() != "y" and startSpam.lower() != "n"):
        startSpam = input("Please enter 'y' or 'n': ")

    if startSpam.lower() == "y":
        spamClick = True
        print(f"Press {keyToggleSpam} to stop spam clicking.\nPress esc to exit the program.")
    else:
        print(f"Press {keyToggleSpam} to start spam clicking.\nPress esc to exit the program.")

    autoClicker(spamFreq, keyToggleSpam)
  

main()