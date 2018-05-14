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
            masterOut.extend(d)
    openFileName = '/../assets/coordoutFinal.txt'
    with open(dirname + openFileName, 'w') as outfile:
        json.dump(masterOut, outfile)
        


def superMunge(mungeIndex):
    latLngArray = []
    openFileName = '/../assets/savecoord'+str(mungeIndex)+'.txt'
    with open(dirname + openFileName) as json_data:
        d = json.load(json_data)
        elementslen = len(d["elements"])
    for x in range(0, elementslen):
        print(d["elements"][x]["lat"])
        point = {'lat': d["elements"][x]["lat"], 'lng': d["elements"][x]["lon"]}
        latLngArray.append(point)

    firstPtIndex = None
    orderedArray = []

    point = {'lat': coordArrayData().coordArray[mungeIndex]['lat'], 'lng': coordArrayData().coordArray[mungeIndex]['lng']}
    orderedArray.append(point)

    getFromLatLngArray = latLngArray
    numSkipped = 0
    avgVal = 0
    avgCounter = 0

    while len(getFromLatLngArray)>0:
        compareToPoint = orderedArray[len(orderedArray)-1]
        print('len(orderedArray)-1')
        print(len(orderedArray)-1)
        print('orderedArray')
        print(orderedArray)
        distance = 9999999999
        svPt = None
        avgCounter = 0
        avgDist = 1
        distTotal = 0
        for x in range(0, len(getFromLatLngArray)):
            compareIngPoint = getFromLatLngArray[x]
            print('compareIngPoint')
            print(compareIngPoint)
            print('compareToPoint')
            print(compareToPoint)
            if not (math.isclose(compareToPoint['lat'], compareIngPoint['lat'], abs_tol=0.000001) and math.isclose(compareToPoint['lng'], compareIngPoint['lng'], abs_tol=0.000001)):
                ptDistance = math.sqrt(math.pow((compareIngPoint['lat']-compareToPoint['lat']),2)+math.pow((compareIngPoint['lng']-compareToPoint['lng']),2))
                if distance>ptDistance: #and (distance<10*avgDist or avgCounter<20):
                    print('inside distance > ptDistance')
                    distance = ptDistance
                    svPt = compareIngPoint
                    # distTotal = distance + distTotal
                    # avgCounter = avgCounter + 1
                    # avgDist = distTotal/avgCounter
                # if distance>=10*avgDist and distance != 9999999999:
                #     numSkipped = numSkipped+1
        # if svPt is not None:
        getFromLatLngArray.remove(svPt)
        orderedArray.append(svPt)

    openFileName = '/../assets/coordout'+str(mungeIndex)+'.txt'

    with open(dirname + openFileName, 'w') as outfile:
        json.dump(orderedArray, outfile)


        # GARBAGE 





        # for x in range(0, len(latLngArray)):
    #     if latLngArray[x]['lat']==coordArrayData().coordArray[mungeIndex]["lat"] and latLngArray[x]['lng']==coordArrayData().coordArray[mungeIndex]["lng"]:
    #         print("inside IF STATEMENT for x loop of ordering")
    #         firstPtIndex = x
    #         orderedArray.append(latLngArray[x])
    #         break

    # def inArrayTester(comparingPt):
    #     notInArray = False
    #     for x in range(0,len(orderedArray)):
    #         if (math.isclose(orderedArray[x]['lat'], comparingPt['lat'], abs_tol=0.000001) and math.isclose(orderedArray[x]['lng'], comparingPt['lng'], abs_tol=0.000001)):
    #             print('found match of already equal!')
    #             print("math.isclose(latLngArray[x]['lat'], comparingPt['lat'], abs_tol=0.000001)")
    #             print(math.isclose(orderedArray[x]['lat'], comparingPt['lat'], abs_tol=0.000001))
    #             print("math.isclose(latLngArray[x]['lng'], comparingPt['lng'], abs_tol=0.000001)")
    #             print(math.isclose(orderedArray[x]['lng'], comparingPt['lng'], abs_tol=0.000001)) 
    #             print('comparingPt')
    #             print(comparingPt)
    #             print('latLngArray[x]')
    #             print(latLngArray[x])
    #             notInArray = True
    #             break
    #     return notInArray

    # def nextPt(testingPt):    
    #     distance = 9999999999
    #     svPt = None
    #     svArray = []
    #     for x in range(0, len(orderedArray)):
    #         comparingPt = orderedArray[x]
    #         alreadyInArrayBool = inArrayTester(comparingPt)
    #         if not alreadyInArrayBool:
    #             ptDistance = math.sqrt(math.pow((testingPt['lat']-comparingPt['lat']),2)+math.pow((testingPt['lng']-comparingPt['lng']),2))
    #             if ptDistance<distance:
    #                 svArray = orderedArray
    #                 distance = ptDistance
    #                 svPt = testingPt 
    #                 print('*****************************************************')
    #                 print("inside svPt")
    #                 print('value of testingPt')
    #                 print(testingPt)
    #                 print('value of testingPt["lat"]')
    #                 print(testingPt['lat'])
    #                 print('value of testingPt["lng"]')
    #                 print(testingPt["lng"])
    #                 print('value of comparingPt')
    #                 print(comparingPt)
    #                 print('value of comparingPt["lat"]')
    #                 print(comparingPt["lat"])
    #                 print('value of comparingPt["lng"]')
    #                 print(comparingPt["lng"])
    #                 print("value of math.isclose(testingPt['lat'], comparingPt['lat'], abs_tol=0.0000001)")
    #                 print(math.isclose(testingPt['lat'], comparingPt['lat'], abs_tol=0.0000001))
    #                 print("value of math.isclose(testingPt['lng'], comparingPt['lng'], abs_tol=0.0000001)")
    #                 print(math.isclose(testingPt['lng'], comparingPt['lng'], abs_tol=0.0000001))
    #                 print("value of not (math.isclose(testingPt['lat'], comparingPt['lat'], abs_tol=0.0000001) and math.isclose(testingPt['lng'], comparingPt['lng'], abs_tol=0.0000001))")
    #                 print(not (math.isclose(testingPt['lat'], comparingPt['lat'], abs_tol=0.0000001) and math.isclose(testingPt['lng'], comparingPt['lng'], abs_tol=0.0000001)))
    #                 print('value of orderedArray')
    #                 print(orderedArray)
    #                 print('value of svPt')
    #                 print(svPt)
    #                 print("*****************************************************")
    #         orderedArray.append(svPt)

    # counter = 0

    # while len(orderedArray)<len(latLngArray):
    #     nextPt(latLngArray[counter])
    #     counter = counter + 1