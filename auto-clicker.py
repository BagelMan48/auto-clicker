#NOW IT DOESNT WORK BUT I SWEAR I CAN FIX IT
#Reminder to self: create a new bool to make autoClicker continuously run
#Reminder to self 2: make that bool be in on_press
#Reminder to self 3: use threading. i can do it
#Reminder to self 4: i can do it. put school as priority first tho!

from pynput import mouse, keyboard
from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, KeyCode, Listener
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

def on_press(key):
    global keyToggleSpamKeyCode
    global spamFreq
    global spamClick

    while (key != Key.esc):
        if key == keyToggleSpamKeyCode:
            spamClick = not spamClick
            if spamClick:
                print("You are spam clicking.")
                mouse_controller.click(clickButton, 1)
            else:
                print("You have stopped spam clicking.")
    print("program stopping")
    return False

# this method might not be needed but we will find out
'''def toggleClick(spamClick):
    showmsg = True
    while (spamClick):
        if showmsg:
            print("You are spam clicking.")
            showmsg = False
        mouse_controller.click(clickButton, 1)
        time.sleep(spamFreq)
    else:
        print("You have stopped spam clicking.")'''


def autoClicker(startClick, spamFreq, keyToggleSpam):

    spamClick = startClick

    global keyToggleSpamKeyCode

    keyToggleSpamKeyCode = KeyCode(char=keyToggleSpam)

    while (spamClick):
        print("You are spam clicking.")
        mouse_controller.click(clickButton, 1)
        time.sleep(spamFreq)
    
    with keyboard.Listener(on_press=on_press,) as listener:
        listener.join()


    '''
    if startClick == True:
        print("You are spam clicking")
        while (startClick == True):
            mouse_controller.click(clickButton, 1)
            if keyboard.pressed(Key[keyToggleSpam]):
                startClick = False
                print("You have stopped clicking.")
            time.sleep(spamFreq)
    else:
        print("You have stopped clicking.")
    '''


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