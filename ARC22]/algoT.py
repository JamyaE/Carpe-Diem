import math
import numpy as np


#if __name__ == '__main__':
#s	main("waypoint_1.txt")


def determinePath(waypoint):
    order = []
    waypointType = waypoint['waypointType']

    #print("waypointType", waypointType)
    #for index in (waypointType):
    #    if index == 'H':
    Hindex = waypointType.index('H')
    print('Hindex', Hindex)

    # COMPLETE HERE
    #42.27690 N -83.73063 E 10 H
    #42.33905 N -83.06404 E 10 Ax
    #42.63678 N -83.29613 E 10 C
    #42.29201 N -83.71624 E 10 B
    #42.29198 N -83.71561 E 10 A
    #if waypointType: i=H save the value?

    Lat0 = float(waypoint['latitude'][0-Hindex])
    Log0 = float(waypoint['longitude'][0-Hindex])
    Alt0 = float(waypoint['altitude'][0-Hindex])
    waypoint0 = 0-Hindex
    print(waypoint0, 'waypoint0')
    Lat1 = float(waypoint['latitude'][1-Hindex])
    Log1 = float(waypoint['longitude'][1-Hindex])
    Alt1 = float(waypoint['altitude'][1-Hindex])
    waypoint1 = 1-Hindex
    print(waypoint1, 'waypoint1')
    Lat2 = float(waypoint['latitude'][2-Hindex])
    Log2 = float(waypoint['longitude'][2-Hindex])
    Alt2 = float(waypoint['altitude'][2-Hindex])
    waypoint2 = 2-Hindex
    print(waypoint2, 'waypoint2')
    Lat3 = float(waypoint['latitude'][3-Hindex])
    Log3 = float(waypoint['longitude'][3-Hindex])
    Alt3 = float(waypoint['altitude'][3-Hindex])
    waypoint3 = 3-Hindex
    print(waypoint3, 'waypoint3')
    Lat4 = float(waypoint['latitude'][4-Hindex])
    Log4 = float(waypoint['longitude'][4-Hindex])
    Alt4 = float(waypoint['altitude'][4-Hindex])
    waypoint4 = 4-Hindex
    print(waypoint4, 'waypoint4')
    #waypointType = waypoint['waypointType']
    #for index in range(len(waypointType)):
    #print(waypointType[index])

    waypointH = np.array((Lat0, Log0, Alt0))
    waypointA = np.array((Lat1, Log1, Alt1))
    waypointC = np.array((Lat2, Log2, Alt2))
    waypointB = np.array((Lat3, Log3, Alt3))
    waypointA2 = np.array((Lat4, Log4, Alt4))

    #if waypointDict{waypointType[i]}
    # if i=H save value

    DistanceHtoA = np.linalg.norm(waypointH-waypointA)
    DistanceHtoC = np.linalg.norm(waypointH-waypointC)
    DistanceHtoB = np.linalg.norm(waypointH-waypointB)
    DistanceHtoA2 = np.linalg.norm(waypointH-waypointA2)
    Distances = [DistanceHtoA, DistanceHtoB,
                 DistanceHtoC, DistanceHtoA2]
    minimumDistances1 = min(Distances)
    if minimumDistances1 == 0:
        order.append(waypoint1)
    elif minimumDistances1 == 1:
        order.append(waypoint3)
    elif minimumDistances1 == 2:
        order.append(waypoint3)
    elif minimumDistances1 == 4:
        order.append(waypoint4)
    print('minimimumDistances1', minimumDistances1)
    print('order', order)

    LatNP = float(waypoint['latitude'][minimumDistances1])
    LogNP = float(waypoint['longitude'][minimumDistances1])
    AltNP = float(waypoint['altitude'][minimumDistances1])
    waypointNP = (LatNP, LogNP, AltNP)
    #P1 = minimumDistances1, "DistanceHtoB"
    #print(minimumDistances1, "minimumDistances1")

    #print("DistanceHtoA ", DistanceHtoA)
    #print("DistanceHtoC", DistanceHtoC)
    #print("DistanceHtoA2", DistanceHtoA2)
    #print("DistanceHtoB", DistanceHtoB)
    #closestwaypoint = Distances.index(minimumDistances)
    #Path = []
    #Path = Path.append(closestwaypoint)
    #Arranged = np.array([[DistanceHtoA, DistanceHtoC,
    #DistanceHtoB, DistanceHtoA2]])

    #print(np.sort(Arranged))

    ####################################
    DistanceNPtoC = np.linalg.norm(waypointNP-waypointC)
    DistanceNPtoA = np.linalg.norm(waypointNP-waypointA)
    DistanceNPtoA2 = np.linalg.norm(waypointNP-waypointA2)
    Distances2 = [DistanceNPtoA, DistanceNPtoC, DistanceNPtoA2]
    minimumDistances2 = min(Distances2)
    print(minimumDistances1)
#    print("minimunDistances2", minimumDistances2)
#    P2 = minimumDistances2, "DistanceBtoA2"
#    print("DistanceBtoC", DistanceBtoC)
#    print("DistanceBtoA", DistanceBtoA)
    #print("DistanceBtoA2", DistanceBtoA2)
    #Arranged2 = np.array([[DistanceAtoC,
    # DistanceAtoB, DistanceAtoA2]])

    #print(np.sort(Arranged2))

    #####################################################

    DistanceA2toA = np.linalg.norm(waypointA2-waypointA)
    DistanceA2toC = np.linalg.norm(waypointA2-waypointC)
    Distances3 = [DistanceA2toA, DistanceA2toC]
    minimumDistances3 = min(Distances3)
#    print("minimunDistances3", minimumDistances3)
#    P3 = minimumDistances3, "DistanceA2toA"
##    print("DistanceA2toA", DistanceA2toA)
#    print("DistanceA2toC", DistanceA2toC)

    ##################################################
    DistanceAtoC = np.linalg.norm(waypointA-waypointC)
    Distances4 = [DistanceAtoC]
    minimumDistances4 = Distances4
#    P4 = minimumDistances4, "DistanceAtoC"

#    Path = ([P1, P2, P3, P4])
    #print(Path)
    #print("This is the waypoint order")
    #return Path
    #order[i]=order[i]+Hindex
    return order
