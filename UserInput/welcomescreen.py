
from .inputchecker import *


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
    while inputLoop == True:
        print("What do you want to do?")
        print("1) Enter coordinates manually")
        print("2) Enter coordinates from file")
        doOption = input("Select: ")
        if doOption == 1:
            print("Enter coordinate values in the following format: ")
            print('[{"lat":<THISPTLATITUDE>, "lng":<THISPTLONGITUDE>}...]')
            coordArray = raw_input("Input: ")
            inputchecker.testInputCoordArray(coordArray)
            inputLoop = False
        elif doOption == 2:
            print("That feature is not yet implemented!")
        else: 
            print("That is not a valid option!")