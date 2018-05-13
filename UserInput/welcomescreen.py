
from .inputchecker import *
from DataClass import *

def welcome():
    print("welcome to ...")
    print("**************************************************************************************************")
    print("                               ___          ___          ___      ")
    print("                              /\  \        /\  \        /\  \     ")
    print("                             /::\  \      /::\  \      /::\  \    ")
    print("                            /:/\:\  \    /:/\:\  \    /:/\ \  \   ")
    print("                           /:/  \:\  \  /::\~\:\  \  _\:\~\ \  \  ")
    print("                          /:/__/_\:\__\/:/\:\ \:\__\/\ \:\ \ \__\ ")
    print("                          \:\  /\ \/__/\/__\:\/:/  /\:\ \:\ \/__/ ")
    print("                           \:\ \:\__\       \::/  /  \:\ \:\__\   ")
    print("                            \:\/:/  /        \/__/    \:\/:/  /   ")
    print("                             \/__/                     \/__/      ")
    print("")
    print("       ___          ___       ___          ___          ___          ___          ___      ")
    print("      /\  \        /\  \     /\  \        /\  \        /\__\        /\  \        /\  \     ")
    print("     /::\  \      /::\  \    \:\  \      /::\  \      /:/  /       /::\  \      /::\  \    ")
    print("    /:/\:\  \    /:/\:\  \    \:\  \    /:/\:\  \    /:/__/       /:/\:\  \    /:/\:\  \   ")
    print("   /::\~\:\  \  /::\~\:\  \   /::\  \  /:/  \:\  \  /::\  \ ___  /::\~\:\  \  /::\~\:\  \  ")
    print("  /:/\:\ \:\__\/:/\:\ \:\__\ /:/\:\__\/:/__/ \:\__\/:/\:\  /\__\/:/\:\ \:\__\/:/\:\ \:\__\ ")
    print("  \/__\:\ \/__/\:\~\:\ \/__//:/  \/__/\:\  \  \/__/\/__\:\/:/  /\:\~\:\ \/__/\/_|::\/:/  / ")
    print("       \:\__\   \:\ \:\__\ /:/  /      \:\  \           \::/  /  \:\ \:\__\     |:|::/  /  ")
    print("        \/__/    \:\ \/__/ \/__/        \:\  \          /:/  /    \:\ \/__/     |:|\/__/   ")
    print("                  \:\__\                 \:\__\        /:/  /      \:\__\       |:|  |     ")
    print("                   \/__/                  \/__/        \/__/        \/__/        \|__|     ")
    print("**************************************************************************************************")
    inputLoop = True
    inputLoop2 = True
    while inputLoop == True:
        print("What do you want to do?")
        print("1) Enter coordinates manually")
        print("2) Enter coordinates from file")
        doOption = input("Select: ")
        print("value of doOption: ")
        try:
            if int(doOption) == 1:
                print("Enter coordinate values in the following format: ")
                print('[{"lat":<THISPTLATITUDE>, "lng":<THISPTLONGITUDE>}...]')
                coordArray = input("Input: ")
                inputLoop = testInputCoordArray(coordArray)
                # while inputLoop2 == True:
                #     print("This runs a selenium driver, how would you like it to run? ")
                #     print("1) Headfull (Show Window Pop Up && Do Stuff)")
                #     print("2) Headless (Nein danke)")
                #     doOption2 = input("Select: ")
                #     try:
                #         if int(doOption2) == 1:
                #             print("Mucho grazzi mi amor, the agreement has been altered")
                #             coordArrayData().setHeadBool(True)
                #             inputLoop2 = False
                #         elif int(doOption) == 2:
                #             print("Mucho grazzi mi amor, the agreement has been altered")
                #             coordArrayData().setHeadBool(False)
                #             inputLoop2 = False
                #         else: 
                #             print("That is not a valid option!")
                #             inputLoop2 = True
                #     except ValueError as e: 
                #         print("Woops, something happened, try again?")
                #         print(e)
                #     inputLoop = testInputCoordArray(coordArray)
            elif int(doOption) == 2:
                print("That feature is not yet implemented!")
            else: 
                print("That is not a valid option!")
        except ValueError as e: 
            print("Woops, something happened, try again?")
            print(e)
