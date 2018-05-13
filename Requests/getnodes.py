


from DataClass import *
from .turbohacker import *
import json
# Example request

# http://router.project-osrm.org/route/v1/driving/-97.729209,30.363562;-97.723990,30.319342;-97.737928,30.193676;-97.933798,25.859127?alternatives=false&annotations=nodes



import requests


def createLegString(legArray):
    legString = 'https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28'
    for x in range(0, len(legArray[0])):
        legString = legString+"node%28"+str(legArray[0][x])+"%29%3B"
    legString = legString + "%29%3B%20%28._%3B%3E%3B%29%3B%20out%3B"
    return legString

# def createLegString(legArray):
#     legString = '[out:json];\n(\n'
#     for x in range(0, len(legArray[0])):
#         legString = legString+"node("+str(legArray[0][x])+");"
#     legString = legString + "); (._;>;); out;"
#     return legString


def postToOSRM():
    print("inside postToOSRM...getting nodes")
    localCoordArray = coordArrayData().coordArray
    requestString = 'http://router.project-osrm.org/route/v1/driving/'
    for x in range(0, len(localCoordArray)):
        requestString = requestString + str(localCoordArray[x]['lng']) + "," + str(localCoordArray[x]['lat'])
        if x == len(localCoordArray) - 1:
            requestString = requestString + '?alternatives=false&annotations=nodes'
        else: 
            requestString = requestString + ";"
    # need error handling on this request?
    print("value of requestString")
    print(requestString)
    r = requests.get(requestString)
    print("returned from getting nodes!")
    print("value of nodes")
    print(r.text)
    resJSON = r.json()
    legStringList = []
    legArray = []
    for y in range(0, len(resJSON['routes'][0]['legs'])):
        legArray.append(resJSON['routes'][0]['legs'][y]['annotation']['nodes'])
        legString = createLegString(legArray)
        legStringList.append(legString)
    print('setting legstringlist in coordarradata class')
    coordArrayData().setLegStringList(legStringList)
    



