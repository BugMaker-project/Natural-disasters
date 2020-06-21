from script import colorfulText,Keys,Error,var
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
        isKeyCorrect=Keys.isIn(Key,Keys.read(Keys.returnObject(vars.PATHS.KeysPaths)))
        if isKeyCorrect:
            with open(vars.PATHS.KeysWrite,"wb") as j:
                j.write(bytes(Key,"utf-8"))
            colorfulText.printGreen("OK\n")
        if not isKeyCorrect:
            colorfulText.printGreen("Incorrect!\n")
    if reponse=="2":
        Codes=input("Enter:")
        listCodes=Keys.read(Keys.returnObject(vars.PATHS.CodesPaths))
        isCodesCorrect=Keys.isIn(Codes,Keys.read(listCodes))
        if isCodesCorrect:
            colorfulText.printGreen("OK\n")
            vars.Controls.ReturnsInXlsx=Keys.read(listCodes)[listCodes.index(Codes)+1]
        if not isCodesCorrect:
            colorfulText.printGreen("Incorrect!\n")
    if reponse=="3":
        pass
    if reponse=="4":
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
