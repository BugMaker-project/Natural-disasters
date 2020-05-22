import colorfulText
import Keys
import Error
import time
def Hi():
    colorfulText.printRed("""
    ###   ###  #########  #########
    ###   ###     ###      #######
    #########     ###       
    #########     ###
    ###   ###     ###       #####
    ###   ###  #########    #####""")
def Intro():
    colorfulText.printWhiteBlack("\nThanks for you choose Natural-Disasters.")
    colorfulText.printWhiteBlack("\nThis is a Menu.")
    colorfulText.printWhiteBlack("\nWe are Bug-Maker Project.")
def Main():
    Hi()
    time.sleep(1)
    Intro()
    time.sleep(3)
Main()
