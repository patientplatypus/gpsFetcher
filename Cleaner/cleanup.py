import os
import json
dirname = os.path.dirname(__file__)
import math

from DataClass import *

def superFresh():
    print("inside superFresh cleanup utility")
    print("now with scrubbing bubbles")

    for x in range(0, len(coordArrayData().coordArray)-1):
        superMunge(x)
    
    masterOut = []

    for x in range(0, len(coordArrayData().coordArray)-1):
        openFileName = '/../assets/coordout'+str(x)+'.txt'
        with open(dirname + openFileName) as json_data:
            d = json.load(json_data)
            masterOut.append(d)
    openFileName = '/../assets/coordoutFinal.json'
    with open(dirname + openFileName, 'w') as outfile:
        json.dump(masterOut[0], outfile)
        


def superMunge(mungeIndex):
    latLngArray = []
    openFileName = '/../assets/savecoord'+str(mungeIndex)+'.txt'
    with open(dirname + openFileName) as json_data:
        d = json.load(json_data)
        # dl = json.loads
        print(d)
        print(d["elements"][0]["lat"])
        elementslen = len(d["elements"])
        print(elementslen)
    for x in range(0, elementslen):
        print(d["elements"][x]["lat"])
        point = {'lat': d["elements"][x]["lat"], 'lng': d["elements"][x]["lon"]}
        latLngArray.append(point)
    
    print('after for loop and value of latLngArray:')
    print(latLngArray)

    print('adding back in original requested points')
    point = {'lat': coordArrayData().coordArray[mungeIndex]['lat'], 'lng': coordArrayData().coordArray[mungeIndex]['lng']}
    latLngArray.append(point)

    firstPtIndex = None
    orderedArray = []
    
    for x in range(0, len(latLngArray)):
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("value of mungeIndex")
        print(mungeIndex)
        print("coordArrayData().coordArray")
        print(coordArrayData().coordArray)
        print("coordArrayData().coordArray[mungeIndex]['lat']")
        print(coordArrayData().coordArray[mungeIndex]['lat'])
        print("latLngArray[x]['lat']")
        print(latLngArray[x]['lat'])
        print("coordArrayData().coordArray[mungeIndex]['lng']")
        print(coordArrayData().coordArray[mungeIndex]['lng'])
        print("latLngArray[x]['lng']")
        print(latLngArray[x]['lng'])
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        if latLngArray[x]['lat']==coordArrayData().coordArray[mungeIndex]["lat"] and latLngArray[x]['lng']==coordArrayData().coordArray[mungeIndex]["lng"]:
            print("inside IF STATEMENT for x loop of ordering")
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
                ptDistance = math.sqrt(math.pow((testingPt['lat']-comparingPt['lat']),2)+math.pow((testingPt['lat']-comparingPt['lat']),2))
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
        print('len(orderedArray)')
        print(len(orderedArray))
        print('len(orderedArray)-1')
        print(str(len(orderedArray)-1))
        nextPt(orderedArray[len(orderedArray)-1], len(orderedArray))

    print('*****************************************************')
    print('after all calculations and final ordered array')
    print('*****************************************************')    

    print(orderedArray)

    print('*****************************************************')
    print('dumping JSON')
    print('*****************************************************')    

    openFileName = '/../assets/coordout'+str(mungeIndex)+'.txt'

    with open(dirname + openFileName, 'w') as outfile:
        json.dump(orderedArray, outfile)