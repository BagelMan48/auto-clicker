#now it half works. it can start the spam click but now it cant stop!

from pynput import mouse, keyboard
from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, KeyCode, Listener
import time

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


def autoClicker(startClick, spamFreq, keyToggleSpam):
    if startClick == True:
        print("You are spam clicking")
        while (startClick == True):
            mouse_controller.click(clickButton, 1)
            time.sleep(spamFreq)
    else:
        print("You have stopped clicking.")


def main():
    keyToggleSpam = input("What key do you want to toggle spam clicking? ")
    while (len(keyToggleSpam) != 1):
        keyToggleSpam = input("Please enter a single character: ")


    spamFreq = spamFrequency()


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