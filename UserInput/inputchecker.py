import json
import emoji

from DataClass import *

def testInputCoordArray(coordArray):
    print("Testing your input type...hold on to your butts")
    coordArray = str(coordArray).replace("'", '"')
    print("value of coordArray in testInputCoordArray:")
    print(coordArray)
    testJSON = json.loads(coordArray)
    allTestsPass = True
    if isinstance(testJSON, list):
        print(emoji.emojize("SUCCESS: inputted value passes list :thumbsup:", use_aliases=True))
        if len(testJSON)<2:
            errorString = ":collision: ERROR: to find GPS between pts you must have at least 2!"
            print(emoji.emojize(errorString, use_aliases=True))
            allTestsPass = False
        else:
            for x in range(0, len(testJSON)):
                if isinstance(testJSON[x], dict):
                    successString = "SUCCESS: found dict in list at place:" + str(x) + " :thumbsup:"
                    print(emoji.emojize(successString, use_aliases=True))
                    if "lat" in testJSON[x]:
                        successString = "SUCCESS: found lat in dict at place:" + str(x) + " :thumbsup:"
                        print(emoji.emojize(successString, use_aliases=True))
                        try: 
                            float(testJSON[x]['lat']) or int(testJSON[x]['lat'])
                            successString = "SUCCESS: lat value is of type float or type int :thumbsup:"
                            print(emoji.emojize(successString, use_aliases=True))
                            if testJSON[x]['lat'] >= -90 or testJSON[x]['lat'] <= 90:
                                successString = "SUCCESS: latitude is within -90 to 90 degrees :thumbsup:"
                                print(emoji.emojize(successString, use_aliases=True))
                            else:
                                errorString = ":collision: ERROR: latitude is NOT within -90 to 90 degrees"
                                print(emoji.emojize(errorString, use_aliases=True))
                                allTestsPass = False
                        except ValueError: 
                            errorString = ":collision: ERROR: lat value is not a number or float and gives error on test of" + str(ValueError)
                            print(emoji.emojize(errorString, use_aliases=True))
                            allTestsPass = False
                    else: 
                        errorString = ":collision: ERROR: no lat in dict at place" + str(x)
                        print(emoji.emojize(errorString, use_aliases=True))
                        allTestsPass = False
                    if "lng" in testJSON[x]:
                        successString = "SUCCESS: found lng in dict at place:" + str(x) + " :thumbsup:"
                        print(emoji.emojize(successString, use_aliases=True))
                        try: 
                            float(testJSON[x]['lng']) or int(testJSON[x]['lng'])
                            successString = "SUCCESS: lng value is of type float or type int :thumbsup:"
                            print(emoji.emojize(successString, use_aliases=True))
                            if testJSON[x]['lng'] >= -180 or testJSON[x]['lng'] <= 180:
                                successString = "SUCCESS: longitude is within -180 to 180 degrees :thumbsup:"
                                print(emoji.emojize(successString, use_aliases=True))
                            else:
                                errorString = ":collision: ERROR: longitude is NOT within -180 to 180 degrees"
                                print(emoji.emojize(errorString, use_aliases=True))
                                allTestsPass = False
                        except ValueError: 
                            errorString = ":collision: ERROR: lng value is not a number or float and gives error on test of" + str(ValueError)
                            print(emoji.emojize(errorString, use_aliases=True))
                            allTestsPass = False
                    else: 
                        errorString = ":collision: ERROR: no lng in dict at place" + str(x)
                        print(emoji.emojize(errorString, use_aliases=True))
                        allTestsPass = False
        if allTestsPass:
            print(emoji.emojize('    :tada: All tests pass :tada:    ', use_aliases=True))
            print("NOW SETTING COORDVAL: ")
            coordDataLocal = coordArrayData()
            coordDataLocal.setCoordArray(testJSON)
            print("AFTER SETTING & VALUE: ")
            print(coordDataLocal.coordArray)
            print(coordArrayData().coordArray[0]['lat'])
            return False
        else: 
            adviceString = ':pray: Please fix errors and reinput!'
            print(emoji.emojize(adviceString, use_aliases=True))
            return True
    else:
        errorString = ":collision: ERROR: your input is not a list!"
        print(emoji.emojize(errorString, use_aliases=True))
        adviceString = ':pray: Please fix errors and reinput!'
        print(emoji.emojize(adviceString, use_aliases=True))
        return True