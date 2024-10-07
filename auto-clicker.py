#I CAN TOGGLE THE CLICKS NOW

from pynput import mouse, keyboard
from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, KeyCode, Listener
import time
import threading
from threading import Thread

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

def on_press(key):
    global program_running
    global keyToggleSpamKeyCode
    global spamFreq
    global spamClick

    if key == keyToggleSpamKeyCode:
        global x
        spamClick = not spamClick

        if spamClick:
            print("You are spam clicking.")
            spamClicking(spamFreq)

        elif (not spamClick):
            print("You have stopped spam clicking.") 

    elif key == Key.esc:
        print("Program stopping")
        program_running = False
        return False

    


def spamClicking(spamFreq):
    global program_running
    program_running = True
    
    global spamClick
    while program_running:
        if (spamClick):
            print("You are spam clicking2.")
            while (spamClick):
                mouse_controller.click(clickButton, 1)
                time.sleep(spamFreq)
        else:
            print("Not spam clicking anymore.")
    
  

def autoClicker(startClick, spamFreq, keyToggleSpam):

    spamClick = startClick

    global keyToggleSpamKeyCode

    keyToggleSpamKeyCode = KeyCode(char=keyToggleSpam)

    global x

    x = threading.Thread(target=spamClicking, args=(spamFreq,))
    
    if spamClick:
        x.start()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    keyToggleSpam = input("What key do you want to toggle spam clicking? ")
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
        print(f"Press {keyToggleSpam} to stop spam clicking.")
    else:
        print(f"Press {keyToggleSpam} to start spam clicking.")


    autoClicker(spamClick, spamFreq, keyToggleSpam)
  

main()