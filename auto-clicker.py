#currently doesn't work. just laying out foundation before implementing the clicker

from pynput import mouse, keyboard


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
    print(f"Fun fact: you will be clicking once every {spamFreq:.2f} seconds.")
    
    return spamFreq



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
    

main()