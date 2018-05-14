import json
import math
import emoji

from UserInput import *
from Requests import *
from Cleaner import *

    

def main():
    welcomescreen.welcome()
    getnodes.postToOSRM()
    turbohacker.goTurbo()
    cleanup.superFresh()



def pythonCleaner():
    print("inside pythonCleaner!")

    # first write to latLngArray array

    latLngArray = []
    elementslen = None
    d = None
    with open('coordfile2.json') as json_data:
        d = json.load(json_data)
        print(d["elements"][0]["lat"])
        elementslen = len(d["elements"])
        print(elementslen)
    for x in range(0, elementslen):
        print(d["elements"][x]["lat"])
        point = {'lat': d["elements"][x]["lat"], 'lng': d["elements"][x]["lon"]}
        latLngArray.append(point)
    print('after for loop and value of latLngArray:')
    print(latLngArray)

    # get index of first point

    # 30.1945795 / -97.73755 starting coordinate!

    firstPtIndex = None
    orderedArray = []
    # math.pow math.sqrt
    
    for x in range(0, len(latLngArray)):
        if latLngArray[x]['lat']==30.1945795 and latLngArray[x]['lng']==-97.73755:
            firstPtIndex = x
            orderedArray.append(latLngArray[x])
            break


    def inOrderedArray(pt, orderedArraylength):
        if orderedArraylength<50:
            for x in range(0, orderedArraylength):
                if pt['lat']==orderedArray[x]["lat"] and  pt['lng']==orderedArray[x]["lng"]:
                    return True
        else:
            for x in range(orderedArraylength-50, orderedArraylength):
                if pt['lat']==orderedArray[x]["lat"] and  pt['lng']==orderedArray[x]["lng"]:
                    return True
        return False

    def nextPt(testingPt, orderedArraylength):    
        distance = 9999999999
        for x in range(0, len(latLngArray)):
            comparingPt = latLngArray[x]
            alreadyInArray = inOrderedArray(comparingPt, orderedArraylength)
            if not alreadyInArray:
                ptDistance = math.sqrt(math.pow((testingPt['lat']-comparingPt['lat']),2)+math.pow((testingPt['lng']-comparingPt['lng']),2))
                if ptDistance<distance:
                    distance = ptDistance
                    svPt = comparingPt 
                # else:
                    # print("distance between points is not smaller")

        print('*****************************************************')
        print('after testing and nextPt to append to orderedArray is')
        print(svPt)
        print("at index number")
        print(len(orderedArray))
        print('*****************************************************')
        orderedArray.append(svPt)

    while len(orderedArray)<len(latLngArray):
        print('*****************************************************')
        print('starting new loop through')
        print('*****************************************************')
        nextPt(orderedArray[len(orderedArray)-1], len(orderedArray))

    print('*****************************************************')
    print('after all calculations and final ordered array')
    print('*****************************************************')    

    print(orderedArray)

    print('*****************************************************')
    print('dumping JSON')
    print('*****************************************************')    

    with open('coordout.json', 'w') as outfile:
        json.dump(orderedArray, outfile)
    

if __name__=="__main__":
    main()
