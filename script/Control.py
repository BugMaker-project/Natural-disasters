import colorfulText
import Keys
import Error
import time,sys
def Hi():
    colorfulText.printRed("""
    ###   ###  #########  #########
    ###   ###     ###      #######
    #########     ###       
    #########     ###
    ###   ###     ###       #####
    ###   ###  #########    #####""")
def Intro():
    colorfulText.printWhiteBlack("\n Thanks for you choose Natural-Disasters.")
    colorfulText.printWhiteBlack("\n This is a Menu.")
    colorfulText.printWhiteBlack("\n We are Bug-Maker Project.")
def Menu():
    colorfulText.printGreen("""
    ###################################
    #1.激活码输入                     #
    #2.作弊码键入                     #
    #3.Devlop Mode                    #
    #4.Exit                           #
    ###################################
    """)
    reponse=input("\n\n\n>>>")
    if reponse=="1":
        Key=input("Enter:")
        isKeyCorrect=Keys.isIn(Key,Keys.read(Keys.returnObject("..//Data//Keys.xls")))
        if isKeyCorrect:
            with open("..//Data//Keys.Key","wb") as j:
                j.write(bytes(Key,"utf-8"))
            colorfulText.printGreen("OK\n")
        else:
            colorfulText.printGreen("Incorrect!\n")
    elif reponse=="2":
        pass
    elif reponse=="3":
        pass
    elif reponse=="4":
        sys.exit()
def Main():
    Hi()
    time.sleep(1)
    Intro()
    time.sleep(3)
    while True:
        Menu()
if __name__=="__main__":
    Main()
